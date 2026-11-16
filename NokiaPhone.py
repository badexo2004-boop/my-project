print("--- NOKIA 5510 MAIN MENU ---")
print("1. Phone book")
print("2. Messages")
print("3. Chat")
print("4. Call register")
print("5. Tones")
print("6. Settings")
print("7. Call divert")
print("8. Music")
print("9. Games")
print("10. Calculator")
print("11. Reminders")
print("12. Clock")
print("13. Profiles")
print("14. Services")
print("15. SIM services")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print()
        print("--- PHONE BOOK ---")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Copy")
        print("7. Assign tone")
        print("8. Send b'card")
        print("9. Options")
        print("10. Speed dials")
        print("11. Voice tags")
        choice_1 = int(input("Enter your choice: "))

        match choice_1:
            case 1:
                print("You selected: Search")
            case 2:
                print("You selected: Service Nos.")
            case 3:
                print("You selected: Add name")
            case 4:
                print("You selected: Erase")
            case 5:
                print("You selected: Edit")
            case 6:
                print("You selected: Copy")
            case 7:
                print("You selected: Assign tone")
            case 8:
                print("You selected: Send b'card")
            case 9:
                print()
                print("--- OPTIONS ---")
                print("1. Memory in use")
                print("2. Type of view")
                print("3. Memory status")
                choice_1_9 = int(input("Enter your choice: "))

                match choice_1_9:
                    case 1:
                        print("You selected: Memory in use")
                    case 2:
                        print("You selected: Type of view")
                    case 3:
                        print("You selected: Memory status")
                    case _:
                        print("Invalid choice.")
            case 10:
                print("You selected: Speed dials")
            case 11:
                print("You selected: Voice tags")
            case _:
                print("Invalid choice.")
    case 2:
        print()
        print("--- MESSAGES ---")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        choice_2 = int(input("Enter your choice: "))

        match choice_2:
            case 1:
                print("You selected: Write messages")
            case 2:
                print("You selected: Inbox")
            case 3:
                print("You selected: Outbox")
            case 4:
                print("You selected: Picture messages")
            case 5:
                print("You selected: Templates")
            case 6:
                print("You selected: Smileys")
            case 7:
                print()
                print("--- MESSAGE SETTINGS ---")
                print("1. Set 1")
                print("2. Common")
                choice_2_7 = int(input("Enter your choice: "))

                match choice_2_7:
                    case 1:
                        print()
                        print("--- SET 1 ---")
                        print("1. Message centre number")
                        print("2. Messages sent as")
                        print("3. Message validity")
                        choice_2_7_1 = int(input("Enter your choice: "))

                        match choice_2_7_1:
                            case 1:
                                print("You selected: Message centre number")
                            case 2:
                                print("You selected: Messages sent as")
                            case 3:
                                print("You selected: Message validity")
                            case _:
                                print("Invalid choice.")
                    case 2:
                        print()
                        print("--- COMMON ---")
                        print("1. Delivery reports")
                        print("2. Reply via same centre")
                        print("3. Character support")
                        choice_2_7_2 = int(input("Enter your choice: "))

                        match choice_2_7_2:
                            case 1:
                                print("You selected: Delivery reports")
                            case 2:
                                print("You selected: Reply via same centre")
                            case 3:
                                print("You selected: Character support")
                            case _:
                                print("Invalid choice.")
                    case _:
                        print("Invalid choice.")
            case 8:
                print("You selected: Info service")
            case 9:
                print("You selected: Voice mailbox number")
            case 10:
                print("You selected: Service command editor")
            case _:
                print("Invalid choice.")
    case 3:
        print("You selected: Chat")
    case 4:
        print()
        print("--- CALL REGISTER ---")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call costs")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        choice_4 = int(input("Enter your choice: "))

        match choice_4:
            case 1:
                print("You selected: Missed calls")
            case 2:
                print("You selected: Received calls")
            case 3:
                print("You selected: Dialled numbers")
            case 4:
                print("You selected: Erase recent call lists")
            case 5:
                print()
                print("--- SHOW CALL DURATION ---")
                print("1. Last call duration")
                print("2. All calls' duration")
                print("3. Received calls' duration")
                print("4. Dialled calls' duration")
                print("5. Clear timers")
                choice_4_5 = int(input("Enter your choice: "))

                match choice_4_5:
                    case 1:
                        print("You selected: Last call duration")
                    case 2:
                        print("You selected: All calls' duration")
                    case 3:
                        print("You selected: Received calls' duration")
                    case 4:
                        print("You selected: Dialled calls' duration")
                    case 5:
                        print("You selected: Clear timers")
                    case _:
                        print("Invalid choice.")
            case 6:
                print()
                print("--- SHOW CALL COSTS ---")
                print("1. Last call cost")
                print("2. All calls' cost")
                print("3. Clear counters")
                choice_4_6 = int(input("Enter your choice: "))

                match choice_4_6:
                    case 1:
                        print("You selected: Last call cost")
                    case 2:
                        print("You selected: All calls' cost")
                    case 3:
                        print("You selected: Clear counters")
                    case _:
                        print("Invalid choice.")
            case 7:
                print()
                print("--- CALL COST SETTINGS ---")
                print("1. Call cost limit")
                print("2. Show costs in")
                choice_4_7 = int(input("Enter your choice: "))

                match choice_4_7:
                    case 1:
                        print("You selected: Call cost limit")
                    case 2:
                        print("You selected: Show costs in")
                    case _:
                        print("Invalid choice.")
            case 8:
                print("You selected: Prepaid credit")
            case _:
                print("Invalid choice.")
    case 5:
        print()
        print("--- TONES ---")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Message alert tone")
        print("5. Keypad tones")
        print("6. Warning tones")
        print("7. Vibrating alert")
        print("8. Screen saver")
        choice_5 = int(input("Enter your choice: "))

        match choice_5:
            case 1:
                print("You selected: Ringing tone")
            case 2:
                print("You selected: Ringing volume")
            case 3:
                print("You selected: Incoming call alert")
            case 4:
                print("You selected: Message alert tone")
            case 5:
                print("You selected: Keypad tones")
            case 6:
                print("You selected: Warning tones")
            case 7:
                print("You selected: Vibrating alert")
            case 8:
                print("You selected: Screen saver")
            case _:
                print("Invalid choice.")
    case 6:
        print()
        print("--- SETTINGS ---")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")
        choice_6 = int(input("Enter your choice: "))

        match choice_6:
            case 1:
                print()
                print("--- CALL SETTINGS ---")
                print("1. Automatic redial")
                print("2. Speed dialling")
                print("3. Call waiting options")
                print("4. Own number sending")
                print("5. Phone line in use")
                print("6. Automatic answer")
                choice_6_1 = int(input("Enter your choice: "))

                match choice_6_1:
                    case 1:
                        print("You selected: Automatic redial")
                    case 2:
                        print("You selected: Speed dialling")
                    case 3:
                        print("You selected: Call waiting options")
                    case 4:
                        print("You selected: Own number sending")
                    case 5:
                        print("You selected: Phone line in use")
                    case 6:
                        print("You selected: Automatic answer")
                    case _:
                        print("Invalid choice.")
            case 2:
                print()
                print("--- PHONE SETTINGS ---")
                print("1. Language")
                print("2. Cell info display")
                print("3. Welcome note")
                print("4. Network selection")
                print("5. Confirm SIM service actions")
                choice_6_2 = int(input("Enter your choice: "))

                match choice_6_2:
                    case 1:
                        print("You selected: Language")
                    case 2:
                        print("You selected: Cell info display")
                    case 3:
                        print("You selected: Welcome note")
                    case 4:
                        print("You selected: Network selection")
                    case 5:
                        print("You selected: Confirm SIM service actions")
                    case _:
                        print("Invalid choice.")
            case 3:
                print()
                print("--- SECURITY SETTINGS ---")
                print("1. PIN code request")
                print("2. Call barring service")
                print("3. Fixed dialling")
                print("4. Closed user group")
                print("5. Security level")
                print("6. Change access codes")
                choice_6_3 = int(input("Enter your choice: "))

                match choice_6_3:
                    case 1:
                        print("You selected: PIN code request")
                    case 2:
                        print("You selected: Call barring service")
                    case 3:
                        print("You selected: Fixed dialling")
                    case 4:
                        print("You selected: Closed user group")
                    case 5:
                        print("You selected: Security level")
                    case 6:
                        print("You selected: Change access codes")
                    case _:
                        print("Invalid choice.")
            case 4:
                print("You selected: Restore factory settings")
            case _:
                print("Invalid choice.")
    case 7:
        print("You selected: Call divert")
    case 8:
        print()
        print("--- MUSIC ---")
        print("1. Music player")
        print("2. Radio")
        print("3. Recorder")
        print("4. Track list")
        choice_8 = int(input("Enter your choice: "))

        match choice_8:
            case 1:
                print("You selected: Music player")
            case 2:
                print("You selected: Radio")
            case 3:
                print("You selected: Recorder")
            case 4:
                print("You selected: Track list")
            case _:
                print("Invalid choice.")
    case 9:
        print("You selected: Games")
    case 10:
        print("You selected: Calculator")
    case 11:
        print("You selected: Reminders")
    case 12:
        print()
        print("--- CLOCK ---")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date setting")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")
        choice_12 = int(input("Enter your choice: "))

        match choice_12:
            case 1:
                print("You selected: Alarm clock")
            case 2:
                print("You selected: Clock settings")
            case 3:
                print("You selected: Date setting")
            case 4:
                print("You selected: Stopwatch")
            case 5:
                print("You selected: Countdown timer")
            case 6:
                print("You selected: Auto update of date and time")
            case _:
                print("Invalid choice.")
    case 13:
        print("You selected: Profiles")
    case 14:
        print("You selected: Services")
    case 15:
        print("You selected: SIM services")
    case _:
        print("Invalid choice.")
