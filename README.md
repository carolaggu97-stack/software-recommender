# Software Recommender

A command-line program that recommends software for a company based on what it needs. It is meant for small businesses and freelancers who are not sure which tools to choose for things like invoicing, payments or project management.

## How it works

The user types the first letters of a business need, such as "inv" or "pay".

- If only one category matches, the program shows the recommended software for it.
- If several categories match, it asks "Did you mean...?" and lists them.
- If nothing matches, it says so and asks again.
- Typing "quit" ends the program.

Example:

    What does the company need? (type the first letters, or 'quit'): p
    Did you mean: payments, project management?

    What does the company need? (type the first letters, or 'quit'): pay

    Recommended programs for payments:
      Stripe
        best for: taking card payments on a website or online store
        price: per-transaction fees, check website

## Categories

- invoicing
- accounting
- crm
- team communication
- website and online store
- scheduling and bookings
- payments
- project management

Each category has three recommended programs, with who each one is best for and a short note on pricing.