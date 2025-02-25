import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print("-" * 80)

for item in data['imdata']:
    dn = item['l1PhysIf']['attributes']['dn']
    desc = item['l1PhysIf']['attributes'].get('descr', '')
    speed = item['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = item['l1PhysIf']['attributes']['mtu']
    print(f"{dn:50} {desc:20} {speed:8} {mtu:6}")