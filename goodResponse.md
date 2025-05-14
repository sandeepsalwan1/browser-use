Question:
Hi, I have a question about the way ActionResult.include_in_memory is handled in the browser-use library, especially in relation to how messages are constructed when using ChatOpenAI with tools.

From what I understand, when a tool is called, the model produces an AIMessage with content='' and a populated tool_calls field. This is followed by an empty ToolMessage. Then, based on the value of include_in_memory, the action result is either:

appended as a HumanMessage (if include_in_memory=True), or

appended as plain text to the state_message (if include_in_memory=False), without being preserved in memory.

I understand that the intention behind include_in_memory is to distinguish between action results that are worth remembering versus those that are not. However, I'm confused about why the result is stored this way.

Specifically, why not put the action result directly in the ToolMessage.content, and if include_in_memory=False, simply clear the content in the next step? The current approach results in a message sequence like:

AIMessage (tool_calls populated, empty content)
ToolMessage (empty)
HumanMessage (tool return value)
which seems a bit unintuitive and breaks the expected structure of messages.

Could someone explain the design rationale behind this structure? Is there a reason why ToolMessage.content isn’t used for the action result?

Thanks in advance!
Answer:
Great question!

Our current ToolMessage (empty) doesn't do anything useful, and exists only to maintain compatibility with the standard tool calling format.

We use 

```
AIMessage (tool_calls populated, empty content)
ToolMessage (empty)
HumanMessage (tool return value)
```


even though most people do

```
AIMessage (tool_calls populated, empty content)
ToolMessage (tool return value)

```


We primarily use HumanMessage (storing everything important like action results, browser state, short+longterm memory) instead because 

1. LLMs are trained to pay special attention to HumanMessages (user input) but may treat ToolMessages as less important. 
2. More LLMs support HumanMessages than tool calling.
3. We can selectively include only some results in memory easily as shown below with include_in_memory flag.



Line 132 `browser_use/agent/message_manager/service.py`:
```

   if result:
       for r in result:
           if r.include_in_memory:
               if r.extracted_content:
                   msg = HumanMessage(content='Action result: ' + str(r.extracted_content))
                   self._add_message_with_tokens(msg)
               if r.error:
                   # ...error handling...
                   msg = HumanMessage(content='Action error: ' + last_line)
                   self._add_message_with_tokens(msg)
               result = None  # if result in history, we dont want to add it again 
```

This pattern gives us maximum flexibility while maintaining compatibility with different LLM architectures. 
