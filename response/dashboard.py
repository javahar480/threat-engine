def show(event, alert=None):
    print("\n=== TRAFFIC ===")
    print(event)
    if alert:
        print("[ALERT]", alert)
