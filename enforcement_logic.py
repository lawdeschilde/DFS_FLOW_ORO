def jurisdiction_anchor():
    anchor = "MICHIGAN_OAKLAND_COUNTY"
    fiduciary_status = "PRIMARY_ACTIVE"
    return f"Jurisdiction: {anchor} | Status: {fiduciary_status}"

if __name__ == "__main__":
    print(jurisdiction_anchor())
