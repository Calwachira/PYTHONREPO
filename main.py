def calculate_car_tax():
    print(" Car Import Tax Calculator ")

    try:
        # Prompt user for input info
        car_model = input("Enter the car model: ")
        cif_value = float(input("Enter the Customs Value (CIF - Cost, Insurance, Freight): "))


        IMPORT_DUTY_RATE = 0.35  # 35% of CIF
        EXCISE_DUTY_RATE = 0.25  # 25% of (CIF + Import Duty)
        VAT_RATE = 0.16  # 16% of (CIF + Import Duty + Excise Duty)
        IDF_RATE = 0.035  # 3.5% of CIF
        RDL_RATE = 0.02  # 2% of CIF

        # Sequential Tax Calculations
        import_duty = cif_value * IMPORT_DUTY_RATE

        excise_value = cif_value + import_duty
        excise_duty = excise_value * EXCISE_DUTY_RATE

        vat_taxable_value = excise_value + excise_duty
        vat_amount = vat_taxable_value * VAT_RATE

        idf_fee = cif_value * IDF_RATE
        rdl_fee = cif_value * RDL_RATE

        total_taxes = import_duty + excise_duty + vat_amount + idf_fee + rdl_fee
        total_landed_cost = cif_value + total_taxes

        # Display results
        print(f"\n--- Tax Breakdown for {car_model} ")
        print(f"Customs Value (CIF): {cif_value:,.2f}")
        print(f"Import Duty (35%):   {import_duty:,.2f}")
        print(f"Excise Duty (25%):   {excise_duty:,.2f}")
        print(f"VAT (16%):           {vat_amount:,.2f}")
        print(f"IDF Fee (3.5%):      {idf_fee:,.2f}")
        print(f"RDL Fee (2%):        {rdl_fee:,.2f}")
        print("-" * 30)
        print(f"Total Taxes Payable: {total_taxes:,.2f}")
        print(f"Total Landed Cost:   {total_landed_cost:,.2f}")

    except ValueError:
        print("Error: Please enter valid numerical values for pricing.")


if __name__ == "__main__":
    calculate_car_tax()
