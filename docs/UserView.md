1. Create Accounts
- Create an account on Heroku.
- Create an account on Supabase.
- Create an account on Stripe.

2. Set Up Supabase
- Create a new project in Supabase.
- Set up the necessary tables (Users, Transactions, etc.) as per the project requirements.
- Note down the Supabase URL and the anon public key for later use.

3. Set Up Stripe
- In the Stripe dashboard, get your API keys.
- Set up a product and pricing for the credits.

4. Set Up Heroku
- Create a new application in Heroku.
- In the settings of your Heroku app, add the following Config Vars:
- SUPABASE_URL: Your Supabase URL
- SUPABASE_KEY: Your Supabase anon public key
- STRIPE_SECRET_KEY: Your Stripe secret key

5. Local Environment Setup
- Clone the APIpeanuts repository.
- Install the required dependencies. 
- Set up the same environment variables (SUPABASE_URL, SUPABASE_KEY, STRIPE_SECRET_KEY) in your local environment.

6. Use the Framework

```python
import apipeanuts

def calculate_cost(param):
    # Define your cost calculation logic here
    return cost

@apipeanuts.pay_per_use(calculate_cost)
def your_function(param):
    # Your function logic here
```