recommendations = {
  "invoicing": [
    {"name": "Holded", "best_for": "small teams that want invoicing and accounting together", "price": "paid, check website"},
    {"name": "Quipu", "best_for": "freelancers and small businesses in Spain", "price": "paid, check website"},
    {"name": "Zoho Invoice", "best_for": "simple invoicing needs", "price": "free plan available"}
  ],
  "accounting": [
    {"name": "Xero", "best_for": "small businesses that want online accounting", "price": "paid, check website"},
    {"name": "QuickBooks", "best_for": "small businesses with growing bookkeeping needs", "price": "paid, check website"},
    {"name": "Holded", "best_for": "companies that want accounting and invoicing in one place", "price": "paid, check website"}
  ],
  "crm": [
    {"name": "HubSpot CRM", "best_for": "teams starting to track clients and sales", "price": "free plan available"},
    {"name": "Pipedrive", "best_for": "sales teams that think in deals and pipelines", "price": "paid, check website"},
    {"name": "Zoho CRM", "best_for": "small businesses that want a flexible CRM", "price": "free plan available"}
  ],
  "team communication": [
    {"name": "Slack", "best_for": "teams that want organized chat channels", "price": "free plan available"},
    {"name": "Microsoft Teams", "best_for": "companies already using Microsoft 365", "price": "check website"},
    {"name": "Google Chat", "best_for": "teams already using Google Workspace", "price": "check website"}
  ],
  "website and online store": [
    {"name": "Shopify", "best_for": "selling products online", "price": "paid, check website"},
    {"name": "WordPress", "best_for": "flexible websites that can grow over time", "price": "free software, hosting costs extra"},
    {"name": "Wix", "best_for": "simple websites built without code", "price": "free plan available"}
  ],
  "scheduling and bookings": [
    {"name": "Calendly", "best_for": "booking meetings and calls", "price": "free plan available"},
    {"name": "Cal.com", "best_for": "teams that want an open-source scheduling tool", "price": "free plan available"},
    {"name": "Acuity Scheduling", "best_for": "service businesses that take paid appointments", "price": "paid, check website"}
  ],
  "payments": [
    {"name": "Stripe", "best_for": "taking card payments on a website or online store", "price": "per-transaction fees, check website"},
    {"name": "PayPal", "best_for": "customers who prefer to pay with their PayPal account", "price": "per-transaction fees, check website"},
    {"name": "SumUp", "best_for": "small businesses that take card payments in person", "price": "card reader plus fees, check website"}
  ],
  "project management": [
    {"name": "Trello", "best_for": "simple task boards for small teams", "price": "free plan available"},
    {"name": "Asana", "best_for": "teams that need to track tasks and deadlines", "price": "free plan available"},
    {"name": "Notion", "best_for": "teams that want notes, tasks and documents in one place", "price": "free plan available"}
  ]
}


class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_word = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for letter in word:
      if letter not in node.children:
        node.children[letter] = TrieNode()
      node = node.children[letter]
    node.is_word = True

  def find_prefix_node(self, prefix):
    node = self.root
    for letter in prefix:
      if letter not in node.children:
        return None
      node = node.children[letter]
    return node

  def collect_words(self, node, current_word, words):
    if node.is_word:
      words.append(current_word)
    for letter in node.children:
      self.collect_words(node.children[letter], current_word + letter, words)


trie = Trie()
for category in recommendations:
  trie.insert(category)


def find_matches(prefix):
  node = trie.find_prefix_node(prefix)
  if node is None:
    return []
  words = []
  trie.collect_words(node, prefix, words)
  return words


def show_recommendations(category):
  print("\nRecommended programs for " + category + ":")
  for program in recommendations[category]:
    print("  " + program["name"])
    print("    best for: " + program["best_for"])
    print("    price: " + program["price"])


def run():
  print("Software recommender")
  while True:
    user_input = input("\nWhat does the company need? (type the first letters, or 'quit'): ").strip().lower()

    if user_input == "quit":
      break
    if user_input == "":
      continue

    matches = find_matches(user_input)

    if len(matches) == 0:
      print("No category starts with that. Try again.")
    elif len(matches) == 1:
      show_recommendations(matches[0])
    else:
      print("Did you mean: " + ", ".join(matches) + "?")


run()