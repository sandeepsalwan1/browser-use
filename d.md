# Handling Sensitive Information in Browser Use

## Managing different website selectors and OTP cases

The selector library approach is ideal for handling different website login forms. You can create a mapping of domains to their specific selectors, allowing your controller action to dynamically select the right elements for each site. For sites not in your library, implementing a fallback mechanism that tries common selector patterns increases reliability.

For OTP handling, implement a human-in-the-loop pattern where your code detects OTP fields and pauses for human input. This can be done by checking for input fields with specific attributes (type="number", maxlength="6", etc.) and then prompting for input: `otp = input("Enter OTP: ")`. Screenshots can be temporarily disabled during sensitive operations by setting `browser.context.config.take_screenshots = False`.

## HTML Content and Sensitive Data Protection

Browser Use passes HTML content to the LLM, which means sensitive data could be exposed even when using the `sensitive_data` parameter. This parameter replaces values in prompts and commands but doesn't sanitize HTML or prevent screenshots from capturing sensitive information.

A comprehensive approach combines: (1) the `sensitive_data` parameter for credential substitution, (2) disabling screenshots during sensitive operations, and (3) HTML sanitization using regex patterns to redact PII before it reaches the LLM. For regions with stricter regulations like Germany, consider implementing a "private browsing mode" that extracts only specific, non-sensitive data rather than sending the entire page context.

## Recommended Approach

Create a dedicated secure controller that handles login flows, with methods for disabling screenshots, sanitizing HTML, and managing human-in-loop interactions for OTP/2FA. This controller should integrate with your selector library for reliable automation across different sites.

For general PII concerns, implement content filtering that redacts sensitive patterns (emails, phone numbers, etc.) before they reach the LLM, while still maintaining enough context for the agent to function effectively. This balanced approach works within Browser Use's constraints while providing strong protection for sensitive information. 