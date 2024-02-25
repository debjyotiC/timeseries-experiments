from consentiumthings import consentiumthings

ct = consentiumthings("53caf802535c7a87")

ct.begin_send("a98a467056c590a22d5d740f89a1c2f2")
ct.send_data([1, 2, 3, 4], ['info1', 'info2', 'info3'])

ct.begin_receive("d46549f155ec2f887066c0ace65b86f2", recent=False)
print(ct.receive_data())
