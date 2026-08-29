import csv

def check_rules(case_id, symptom, show_output):
    findings = []
    output_lower = show_output.lower()
    
    if "admin down" in output_lower or "disconnected" in output_lower:
        findings.append("ALERT: Physical interface is down or disconnected (Layer 1 issue).")
        
    if "169.254" in show_output:
        findings.append("ALERT: Device has an APIPA address (169.254.x.x). DHCP has failed.")
        
    if "deny icmp" in output_lower or "deny tcp" in output_lower:
        findings.append("ALERT: Access Control List (ACL) is explicitly denying traffic.")
        
    if "vlan 99" in output_lower:
        findings.append("ALERT: Device is assigned to the wrong VLAN (VLAN 99 detected).")
        
    if "null0" in output_lower:
        findings.append("ALERT: Traffic is being routed to Null0 (Blackhole route detected).")

    if not findings:
        findings.append("No obvious deterministic errors found. Handing over to AI for deep diagnosis.")
        
    return findings

def main():
    print("="*50)
    print("      NetSage AI - Rule Checker Started")
    print("="*50)
    
    try:
        with open('cases.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                case_id = row['Case_ID']
                symptom = row['Symptom_Description']
                show_output = row['Show_Command_Output']
                
                alerts = check_rules(case_id, symptom, show_output)
                
                print(f"\n[{case_id}] Symptom: {symptom[:60]}...")
                for alert in alerts:
                    print(f"  -> {alert}")
                    
        print("\n" + "="*50)
        print("      Rule Check Complete!")
        print("="*50)
                    
    except FileNotFoundError:
        print("ERROR: cases.csv not found!")
        print("Please make sure 'cases.csv' is in the exact same folder as this Python script.")

main()