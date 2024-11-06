import pandas as pd
import send
import make_pairs


def convert_excel_to_dict():
    # Read the excel file
    df=pd.read_excel("example.xlsx")
    
    # Convert the dataframe to a dictionary
    try:
        data_dict=df.to_dict(orient="records")
        
        # Check the values
        for elem in data_dict:
            for cat in elem:
                if cat == 'Telefon': # Check if the phone number is valid
                    elem[cat] = str(elem[cat])
                    elem[cat] = "+40" + elem[cat]
                    data_dict[data_dict.index(elem)] = elem
                if pd.isna(elem[cat]): # Check if the value is NaN
                    elem[cat] = " "
                    data_dict[data_dict.index(elem)] = elem
                if elem[cat].count(")") > 0: # Check if the value contains parentheses
                    elem[cat] = elem[cat].replace(")",">")
                    data_dict[data_dict.index(elem)] = elem
                if elem[cat].count("(") > 0: # Check if the value contains parentheses
                    elem[cat] = elem[cat].replace("(","<")
                    data_dict[data_dict.index(elem)] = elem

        # Make pairs
        pairs=make_pairs.make_pairs(data_dict)
        
        # Extract phone numbers
        phone_numbers = []
        for elem in pairs:
            phone_numbers.append(elem["Telefon"])
        
        # Send the messages
        send.send_msg(phone_numbers, pairs)
    
    except FileNotFoundError:
        print("Fisierul nu a fost gasit")
        
    except Exception as e:
        print(f"A aparut o eroare: {e}")
            
if __name__ == "__main__":
    convert_excel_to_dict()