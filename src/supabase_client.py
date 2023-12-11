# src/supabase_client.py
from supabase import create_client
from .config import SUPABASE_URL, SUPABASE_KEY

def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)
