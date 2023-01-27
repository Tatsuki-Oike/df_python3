import traceback

try:
    print(Hello)
except Exception as e:
    print(f"ERROR : {e}")

try:
    print(Hello)
except Exception:
    print(f"ERROR : {traceback.format_exc()}")