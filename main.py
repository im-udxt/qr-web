import qrcode

def html_to_qr(output_file):
    """
    Converts an HTML file to a QR code.

    Parameters:
    input_file (str): Path to the HTML file to convert.
    output_file (str): Path to save the generated QR code image.
    """
    try:
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # Adjust this for more complex data
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("data:text/html;base64,PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KICA8dGl0bGU+VGlwIENhbGN1bGF0b3I8L3RpdGxlPgogIDxzdHlsZT4KICAgIGJvZHkgeyBmb250LWZhbWlseTogQXJpYWwsIHNhbnMtc2VyaWY7IHRleHQtYWxpZ246IGNlbnRlcjsgbWFyZ2luOiAyMHB4OyB9CiAgICBpbnB1dCB7IG1hcmdpbjogNXB4OyBwYWRkaW5nOiA4cHg7IH0KICAgIC5vdXRwdXQgeyBtYXJnaW4tdG9wOiAyMHB4OyB9CiAgPC9zdHlsZT4KPC9oZWFkPgo8Ym9keT4KICA8aDE+VGlwIENhbGN1bGF0b3I8L2gxPgogIDxsYWJlbD5CaWxsIEFtb3VudDogJDxpbnB1dCBpZD0iYmlsbCIgdHlwZT0ibnVtYmVyIiBzdGVwPSIwLjAxIj48L2xhYmVsPjxicj4KICA8bGFiZWw+VGlwIFBlcmNlbnRhZ2U6IAogICAgPHNlbGVjdCBpZD0idGlwIj4KICAgICAgPG9wdGlvbiB2YWx1ZT0iMC4xIj4xMCU8L29wdGlvbj4KICAgICAgPG9wdGlvbiB2YWx1ZT0iMC4xNSIgc2VsZWN0ZWQ+MTUlPC9vcHRpb24+CiAgICAgIDxvcHRpb24gdmFsdWU9IjAuMiI+MjAlPC9vcHRpb24+CiAgICAgIDxvcHRpb24gdmFsdWU9ImN1c3RvbSI+Q3VzdG9tPC9vcHRpb24+CiAgICA8L3NlbGVjdD4KICA8L2xhYmVsPjxicj4KICA8bGFiZWwgaWQ9ImN1c3RvbS10aXAtbGFiZWwiIHN0eWxlPSJkaXNwbGF5Om5vbmU7Ij5DdXN0b20gVGlwICU6IDxpbnB1dCBpZD0iY3VzdG9tLXRpcCIgdHlwZT0ibnVtYmVyIiBzdGVwPSIxIj48L2xhYmVsPjxicj4KICA8bGFiZWw+TnVtYmVyIG9mIFBlb3BsZTogPGlucHV0IGlkPSJwZW9wbGUiIHR5cGU9Im51bWJlciIgdmFsdWU9IjEiPjwvbGFiZWw+PGJyPgogIDxidXR0b24gb25jbGljaz0iY2FsY3VsYXRlVGlwKCkiPkNhbGN1bGF0ZTwvYnV0dG9uPgoKICA8ZGl2IGNsYXNzPSJvdXRwdXQiIGlkPSJvdXRwdXQiPjwvZGl2PgoKICA8c2NyaXB0PgogICAgY29uc3QgdGlwRHJvcGRvd24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgndGlwJyk7CiAgICBjb25zdCBjdXN0b21UaXBMYWJlbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdjdXN0b20tdGlwLWxhYmVsJyk7CgogICAgdGlwRHJvcGRvd24uYWRkRXZlbnRMaXN0ZW5lcignY2hhbmdlJywgKCkgPT4gewogICAgICBjdXN0b21UaXBMYWJlbC5zdHlsZS5kaXNwbGF5ID0gdGlwRHJvcGRvd24udmFsdWUgPT09ICdjdXN0b20nID8gJ2lubGluZScgOiAnbm9uZSc7CiAgICB9KTsKCiAgICBmdW5jdGlvbiBjYWxjdWxhdGVUaXAoKSB7CiAgICAgIGNvbnN0IGJpbGwgPSBwYXJzZUZsb2F0KGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdiaWxsJykudmFsdWUpIHx8IDA7CiAgICAgIGxldCB0aXBQZXJjZW50ID0gcGFyc2VGbG9hdCh0aXBEcm9wZG93bi52YWx1ZSk7CiAgICAgIGlmICh0aXBEcm9wZG93bi52YWx1ZSA9PT0gJ2N1c3RvbScpIHsKICAgICAgICB0aXBQZXJjZW50ID0gKHBhcnNlRmxvYXQoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2N1c3RvbS10aXAnKS52YWx1ZSkgfHwgMCkgLyAxMDA7CiAgICAgIH0KICAgICAgY29uc3QgcGVvcGxlID0gcGFyc2VJbnQoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3Blb3BsZScpLnZhbHVlKSB8fCAxOwoKICAgICAgY29uc3QgdGlwQW1vdW50ID0gYmlsbCAqIHRpcFBlcmNlbnQ7CiAgICAgIGNvbnN0IHRvdGFsID0gYmlsbCArIHRpcEFtb3VudDsKICAgICAgY29uc3QgcGVyUGVyc29uID0gdG90YWwgLyBwZW9wbGU7CgogICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnb3V0cHV0JykuaW5uZXJIVE1MID0gYAogICAgICAgIDxwPlRpcCBBbW91bnQ6ICQke3RpcEFtb3VudC50b0ZpeGVkKDIpfTwvcD4KICAgICAgICA8cD5Ub3RhbCBCaWxsOiAkJHt0b3RhbC50b0ZpeGVkKDIpfTwvcD4KICAgICAgICA8cD5FYWNoIFBlcnNvbiBPd2VzOiAkJHtwZXJQZXJzb24udG9GaXhlZCgyKX08L3A+CiAgICAgIGA7CiAgICB9CiAgPC9zY3JpcHQ+CjwvYm9keT4KPC9odG1sPgo=")
        qr.make(fit=True)

        # Create and save the QR code image
        img = qr.make_image(fill='black', back_color='white')
        img.save(output_file)

        print(f"QR code generated and saved as {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


output_qr = "tip_calculator_qr.png"  # Output QR code image file
html_to_qr( output_qr)