# Nokia 5510 menu map
# - each menu is a while loop, a submenu is a while loop inside it
# - type the item number like the shortcut keys on the phone
# - 0 = go back, 99 = leave the menu completely
# - choices are kept as text so typing letters will not crash it

quit_all = False    # turns True when the user types 99

print("Welcome to the Nokia 5510 menu.")
main_choice = ""
while main_choice != "0" and not quit_all:
    print()
    print("==============================")
    print(" MAIN MENU")
    print("==============================")
    print("   1. Phone book ...")
    print("   2. Messages ...")
    print("   3. Chat")
    print("   4. Call register ...")
    print("   5. Tones ...")
    print("   6. Settings ...")
    print("   7. Call divert")
    print("   8. Music ...")
    print("   9. Games")
    print("  10. Calculator")
    print("  11. Reminders")
    print("  12. Clock ...")
    print("  13. Profiles")
    print("  14. Services")
    print("  15. SIM services")
    main_choice = input("Item number (0 = back, 99 = exit): ")
    if main_choice == "99":
        quit_all = True
    elif main_choice == "1":
        # Phone book
        choice2 = ""
        while choice2 != "0" and not quit_all:
            print()
            print("==============================")
            print(" 1 PHONE BOOK")
            print("==============================")
            print("   1. Search")
            print("   2. Service Nos.")
            print("   3. Add name")
            print("   4. Erase")
            print("   5. Edit")
            print("   6. Copy")
            print("   7. Assign tone")
            print("   8. Send b'card")
            print("   9. Options ...")
            print("  10. Speed dials")
            print("  11. Voice tags")
            choice2 = input("Item number (0 = back, 99 = exit): ")
            if choice2 == "99":
                quit_all = True
            elif choice2 == "9":
                # Options
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 1-9 OPTIONS")
                    print("==============================")
                    print("   1. Memory in use")
                    print("   2. Type of view")
                    print("   3. Memory status")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 != "0":
                        item = ""
                        if choice3 == "1":
                            item = "Memory in use"
                        elif choice3 == "2":
                            item = "Type of view"
                        elif choice3 == "3":
                            item = "Memory status"
                        if item == "":
                            print("Enter a number from 0 to 3.")
                        else:
                            print()
                            print(f"*** {item} ***  (shortcut 1-9-{choice3})")
                            print("(function would run here)")
            elif choice2 != "0":
                item = ""
                if choice2 == "1":
                    item = "Search"
                elif choice2 == "2":
                    item = "Service Nos."
                elif choice2 == "3":
                    item = "Add name"
                elif choice2 == "4":
                    item = "Erase"
                elif choice2 == "5":
                    item = "Edit"
                elif choice2 == "6":
                    item = "Copy"
                elif choice2 == "7":
                    item = "Assign tone"
                elif choice2 == "8":
                    item = "Send b'card"
                elif choice2 == "10":
                    item = "Speed dials"
                elif choice2 == "11":
                    item = "Voice tags"
                if item == "":
                    print("Enter a number from 0 to 11.")
                else:
                    print()
                    print(f"*** {item} ***  (shortcut 1-{choice2})")
                    print("(function would run here)")
    elif main_choice == "2":
        # Messages
        choice2 = ""
        while choice2 != "0" and not quit_all:
            print()
            print("==============================")
            print(" 2 MESSAGES")
            print("==============================")
            print("   1. Write messages")
            print("   2. Inbox")
            print("   3. Outbox")
            print("   4. Picture messages")
            print("   5. Templates")
            print("   6. Smileys")
            print("   7. Message settings ...")
            print("   8. Info service")
            print("   9. Voice mailbox number")
            print("  10. Service command editor")
            choice2 = input("Item number (0 = back, 99 = exit): ")
            if choice2 == "99":
                quit_all = True
            elif choice2 == "7":
                # Message settings
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 2-7 MESSAGE SETTINGS")
                    print("==============================")
                    print("   1. Set 1 ...")
                    print("   2. Common ...")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 == "1":
                        # Set 1
                        choice4 = ""
                        while choice4 != "0" and not quit_all:
                            print()
                            print("==============================")
                            print(" 2-7-1 SET 1")
                            print("==============================")
                            print("   1. Message centre number")
                            print("   2. Messages sent as")
                            print("   3. Message validity")
                            choice4 = input("Item number (0 = back, 99 = exit): ")
                            if choice4 == "99":
                                quit_all = True
                            elif choice4 != "0":
                                item = ""
                                if choice4 == "1":
                                    item = "Message centre number"
                                elif choice4 == "2":
                                    item = "Messages sent as"
                                elif choice4 == "3":
                                    item = "Message validity"
                                if item == "":
                                    print("Enter a number from 0 to 3.")
                                else:
                                    print()
                                    print(f"*** {item} ***  (shortcut 2-7-1-{choice4})")
                                    print("(function would run here)")
                    elif choice3 == "2":
                        # Common
                        choice4 = ""
                        while choice4 != "0" and not quit_all:
                            print()
                            print("==============================")
                            print(" 2-7-2 COMMON")
                            print("==============================")
                            print("   1. Delivery reports")
                            print("   2. Reply via same centre")
                            print("   3. Character support")
                            choice4 = input("Item number (0 = back, 99 = exit): ")
                            if choice4 == "99":
                                quit_all = True
                            elif choice4 != "0":
                                item = ""
                                if choice4 == "1":
                                    item = "Delivery reports"
                                elif choice4 == "2":
                                    item = "Reply via same centre"
                                elif choice4 == "3":
                                    item = "Character support"
                                if item == "":
                                    print("Enter a number from 0 to 3.")
                                else:
                                    print()
                                    print(f"*** {item} ***  (shortcut 2-7-2-{choice4})")
                                    print("(function would run here)")
                    elif choice3 != "0":
                        print("Enter a number from 0 to 2.")
            elif choice2 != "0":
                item = ""
                if choice2 == "1":
                    item = "Write messages"
                elif choice2 == "2":
                    item = "Inbox"
                elif choice2 == "3":
                    item = "Outbox"
                elif choice2 == "4":
                    item = "Picture messages"
                elif choice2 == "5":
                    item = "Templates"
                elif choice2 == "6":
                    item = "Smileys"
                elif choice2 == "8":
                    item = "Info service"
                elif choice2 == "9":
                    item = "Voice mailbox number"
                elif choice2 == "10":
                    item = "Service command editor"
                if item == "":
                    print("Enter a number from 0 to 10.")
                else:
                    print()
                    print(f"*** {item} ***  (shortcut 2-{choice2})")
                    print("(function would run here)")
    elif main_choice == "4":
        # Call register
        choice2 = ""
        while choice2 != "0" and not quit_all:
            print()
            print("==============================")
            print(" 4 CALL REGISTER")
            print("==============================")
            print("   1. Missed calls")
            print("   2. Received calls")
            print("   3. Dialled numbers")
            print("   4. Erase recent call lists")
            print("   5. Show call duration ...")
            print("   6. Show call costs ...")
            print("   7. Call cost settings ...")
            print("   8. Prepaid credit")
            choice2 = input("Item number (0 = back, 99 = exit): ")
            if choice2 == "99":
                quit_all = True
            elif choice2 == "5":
                # Show call duration
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 4-5 SHOW CALL DURATION")
                    print("==============================")
                    print("   1. Last call duration")
                    print("   2. All calls' duration")
                    print("   3. Received calls' duration")
                    print("   4. Dialled calls' duration")
                    print("   5. Clear timers")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 != "0":
                        item = ""
                        if choice3 == "1":
                            item = "Last call duration"
                        elif choice3 == "2":
                            item = "All calls' duration"
                        elif choice3 == "3":
                            item = "Received calls' duration"
                        elif choice3 == "4":
                            item = "Dialled calls' duration"
                        elif choice3 == "5":
                            item = "Clear timers"
                        if item == "":
                            print("Enter a number from 0 to 5.")
                        else:
                            print()
                            print(f"*** {item} ***  (shortcut 4-5-{choice3})")
                            print("(function would run here)")
            elif choice2 == "6":
                # Show call costs
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 4-6 SHOW CALL COSTS")
                    print("==============================")
                    print("   1. Last call cost")
                    print("   2. All calls' cost")
                    print("   3. Clear counters")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 != "0":
                        item = ""
                        if choice3 == "1":
                            item = "Last call cost"
                        elif choice3 == "2":
                            item = "All calls' cost"
                        elif choice3 == "3":
                            item = "Clear counters"
                        if item == "":
                            print("Enter a number from 0 to 3.")
                        else:
                            print()
                            print(f"*** {item} ***  (shortcut 4-6-{choice3})")
                            print("(function would run here)")
            elif choice2 == "7":
                # Call cost settings
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 4-7 CALL COST SETTINGS")
                    print("==============================")
                    print("   1. Call cost limit")
                    print("   2. Show costs in")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 != "0":
                        item = ""
                        if choice3 == "1":
                            item = "Call cost limit"
                        elif choice3 == "2":
                            item = "Show costs in"
                        if item == "":
                            print("Enter a number from 0 to 2.")
                        else:
                            print()
                            print(f"*** {item} ***  (shortcut 4-7-{choice3})")
                            print("(function would run here)")
            elif choice2 != "0":
                item = ""
                if choice2 == "1":
                    item = "Missed calls"
                elif choice2 == "2":
                    item = "Received calls"
                elif choice2 == "3":
                    item = "Dialled numbers"
                elif choice2 == "4":
                    item = "Erase recent call lists"
                elif choice2 == "8":
                    item = "Prepaid credit"
                if item == "":
                    print("Enter a number from 0 to 8.")
                else:
                    print()
                    print(f"*** {item} ***  (shortcut 4-{choice2})")
                    print("(function would run here)")
    elif main_choice == "5":
        # Tones
        choice2 = ""
        while choice2 != "0" and not quit_all:
            print()
            print("==============================")
            print(" 5 TONES")
            print("==============================")
            print("   1. Ringing tone")
            print("   2. Ringing volume")
            print("   3. Incoming call alert")
            print("   4. Message alert tone")
            print("   5. Keypad tones")
            print("   6. Warning tones")
            print("   7. Vibrating alert")
            print("   8. Screen saver")
            choice2 = input("Item number (0 = back, 99 = exit): ")
            if choice2 == "99":
                quit_all = True
            elif choice2 != "0":
                item = ""
                if choice2 == "1":
                    item = "Ringing tone"
                elif choice2 == "2":
                    item = "Ringing volume"
                elif choice2 == "3":
                    item = "Incoming call alert"
                elif choice2 == "4":
                    item = "Message alert tone"
                elif choice2 == "5":
                    item = "Keypad tones"
                elif choice2 == "6":
                    item = "Warning tones"
                elif choice2 == "7":
                    item = "Vibrating alert"
                elif choice2 == "8":
                    item = "Screen saver"
                if item == "":
                    print("Enter a number from 0 to 8.")
                else:
                    print()
                    print(f"*** {item} ***  (shortcut 5-{choice2})")
                    print("(function would run here)")
    elif main_choice == "6":
        # Settings
        choice2 = ""
        while choice2 != "0" and not quit_all:
            print()
            print("==============================")
            print(" 6 SETTINGS")
            print("==============================")
            print("   1. Call settings ...")
            print("   2. Phone settings ...")
            print("   3. Security settings ...")
            print("   4. Restore factory settings")
            choice2 = input("Item number (0 = back, 99 = exit): ")
            if choice2 == "99":
                quit_all = True
            elif choice2 == "1":
                # Call settings
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 6-1 CALL SETTINGS")
                    print("==============================")
                    print("   1. Automatic redial")
                    print("   2. Speed dialling")
                    print("   3. Call waiting options")
                    print("   4. Own number sending")
                    print("   5. Phone line in use")
                    print("   6. Automatic answer")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 != "0":
                        item = ""
                        if choice3 == "1":
                            item = "Automatic redial"
                        elif choice3 == "2":
                            item = "Speed dialling"
                        elif choice3 == "3":
                            item = "Call waiting options"
                        elif choice3 == "4":
                            item = "Own number sending"
                        elif choice3 == "5":
                            item = "Phone line in use"
                        elif choice3 == "6":
                            item = "Automatic answer"
                        if item == "":
                            print("Enter a number from 0 to 6.")
                        else:
                            print()
                            print(f"*** {item} ***  (shortcut 6-1-{choice3})")
                            print("(function would run here)")
            elif choice2 == "2":
                # Phone settings
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 6-2 PHONE SETTINGS")
                    print("==============================")
                    print("   1. Language")
                    print("   2. Cell info display")
                    print("   3. Welcome note")
                    print("   4. Network selection")
                    print("   5. Confirm SIM service actions")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 != "0":
                        item = ""
                        if choice3 == "1":
                            item = "Language"
                        elif choice3 == "2":
                            item = "Cell info display"
                        elif choice3 == "3":
                            item = "Welcome note"
                        elif choice3 == "4":
                            item = "Network selection"
                        elif choice3 == "5":
                            item = "Confirm SIM service actions"
                        if item == "":
                            print("Enter a number from 0 to 5.")
                        else:
                            print()
                            print(f"*** {item} ***  (shortcut 6-2-{choice3})")
                            print("(function would run here)")
            elif choice2 == "3":
                # Security settings
                choice3 = ""
                while choice3 != "0" and not quit_all:
                    print()
                    print("==============================")
                    print(" 6-3 SECURITY SETTINGS")
                    print("==============================")
                    print("   1. PIN code request")
                    print("   2. Call barring service")
                    print("   3. Fixed dialling")
                    print("   4. Closed user group")
                    print("   5. Security level")
                    print("   6. Change access codes")
                    choice3 = input("Item number (0 = back, 99 = exit): ")
                    if choice3 == "99":
                        quit_all = True
                    elif choice3 != "0":
                        item = ""
                        if choice3 == "1":
                            item = "PIN code request"
                        elif choice3 == "2":
                            item = "Call barring service"
                        elif choice3 == "3":
                            item = "Fixed dialling"
                        elif choice3 == "4":
                            item = "Closed user group"
                        elif choice3 == "5":
                            item = "Security level"
                        elif choice3 == "6":
                            item = "Change access codes"
                        if item == "":
                            print("Enter a number from 0 to 6.")
                        else:
                            print()
                            print(f"*** {item} ***  (shortcut 6-3-{choice3})")
                            print("(function would run here)")
            elif choice2 != "0":
                item = ""
                if choice2 == "4":
                    item = "Restore factory settings"
                if item == "":
                    print("Enter a number from 0 to 4.")
                else:
                    print()
                    print(f"*** {item} ***  (shortcut 6-{choice2})")
                    print("(function would run here)")
    elif main_choice == "8":
        # Music
        choice2 = ""
        while choice2 != "0" and not quit_all:
            print()
            print("==============================")
            print(" 8 MUSIC")
            print("==============================")
            print("   1. Music player")
            print("   2. Radio")
            print("   3. Recorder")
            print("   4. Track list")
            choice2 = input("Item number (0 = back, 99 = exit): ")
            if choice2 == "99":
                quit_all = True
            elif choice2 != "0":
                item = ""
                if choice2 == "1":
                    item = "Music player"
                elif choice2 == "2":
                    item = "Radio"
                elif choice2 == "3":
                    item = "Recorder"
                elif choice2 == "4":
                    item = "Track list"
                if item == "":
                    print("Enter a number from 0 to 4.")
                else:
                    print()
                    print(f"*** {item} ***  (shortcut 8-{choice2})")
                    print("(function would run here)")
    elif main_choice == "12":
        # Clock
        choice2 = ""
        while choice2 != "0" and not quit_all:
            print()
            print("==============================")
            print(" 12 CLOCK")
            print("==============================")
            print("   1. Alarm clock")
            print("   2. Clock settings")
            print("   3. Date setting")
            print("   4. Stopwatch")
            print("   5. Countdown timer")
            print("   6. Auto update of date and time")
            choice2 = input("Item number (0 = back, 99 = exit): ")
            if choice2 == "99":
                quit_all = True
            elif choice2 != "0":
                item = ""
                if choice2 == "1":
                    item = "Alarm clock"
                elif choice2 == "2":
                    item = "Clock settings"
                elif choice2 == "3":
                    item = "Date setting"
                elif choice2 == "4":
                    item = "Stopwatch"
                elif choice2 == "5":
                    item = "Countdown timer"
                elif choice2 == "6":
                    item = "Auto update of date and time"
                if item == "":
                    print("Enter a number from 0 to 6.")
                else:
                    print()
                    print(f"*** {item} ***  (shortcut 12-{choice2})")
                    print("(function would run here)")
    elif main_choice != "0":
        item = ""
        if main_choice == "3":
            item = "Chat"
        elif main_choice == "7":
            item = "Call divert"
        elif main_choice == "9":
            item = "Games"
        elif main_choice == "10":
            item = "Calculator"
        elif main_choice == "11":
            item = "Reminders"
        elif main_choice == "13":
            item = "Profiles"
        elif main_choice == "14":
            item = "Services"
        elif main_choice == "15":
            item = "SIM services"
        if item == "":
            print("Enter a number from 0 to 15.")
        else:
            print()
            print(f"*** {item} ***  (shortcut {main_choice})")
            print("(function would run here)")

print("Back to standby mode.")
