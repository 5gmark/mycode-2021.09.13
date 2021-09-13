#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print("New List: ", *new_list)
print(*new_list)

#!/usr/bin/env python3

def main():
    # below is a lists of lists containing the drivers needed to connect to
    # the switch IP addresses
    networklists = [['ios', '10.0.2.1'], ['ios', '10.0.55.1'], ['ios-xr', '10.0.3.1'], ['junos', '10.0.10.1'], ['eos', '10.0.14.1']]

    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
