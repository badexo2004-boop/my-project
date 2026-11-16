import java.util.Scanner;

public class NokiaMenu {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println();
        System.out.println("--- NOKIA 5510 MAIN MENU ---");
        System.out.println("1. Phone book");
        System.out.println("2. Messages");
        System.out.println("3. Chat");
        System.out.println("4. Call register");
        System.out.println("5. Tones");
        System.out.println("6. Settings");
        System.out.println("7. Call divert");
        System.out.println("8. Music");
        System.out.println("9. Games");
        System.out.println("10. Calculator");
        System.out.println("11. Reminders");
        System.out.println("12. Clock");
        System.out.println("13. Profiles");
        System.out.println("14. Services");
        System.out.println("15. SIM services");
        System.out.print("Enter your choice: ");
        int choice = input.nextInt();

        switch (choice) {
            case 1:
                System.out.println();
                System.out.println("--- PHONE BOOK ---");
                System.out.println("1. Search");
                System.out.println("2. Service Nos.");
                System.out.println("3. Add name");
                System.out.println("4. Erase");
                System.out.println("5. Edit");
                System.out.println("6. Copy");
                System.out.println("7. Assign tone");
                System.out.println("8. Send b'card");
                System.out.println("9. Options");
                System.out.println("10. Speed dials");
                System.out.println("11. Voice tags");
                System.out.print("Enter your choice: ");
                int choice_1 = input.nextInt();

                switch (choice_1) {
                    case 1:
                        System.out.println("You selected: Search");
                        break;
                    case 2:
                        System.out.println("You selected: Service Nos.");
                        break;
                    case 3:
                        System.out.println("You selected: Add name");
                        break;
                    case 4:
                        System.out.println("You selected: Erase");
                        break;
                    case 5:
                        System.out.println("You selected: Edit");
                        break;
                    case 6:
                        System.out.println("You selected: Copy");
                        break;
                    case 7:
                        System.out.println("You selected: Assign tone");
                        break;
                    case 8:
                        System.out.println("You selected: Send b'card");
                        break;
                    case 9:
                        System.out.println();
                        System.out.println("--- OPTIONS ---");
                        System.out.println("1. Memory in use");
                        System.out.println("2. Type of view");
                        System.out.println("3. Memory status");
                        System.out.print("Enter your choice: ");
                        int choice_1_9 = input.nextInt();

                        switch (choice_1_9) {
                            case 1:
                                System.out.println("You selected: Memory in use");
                                break;
                            case 2:
                                System.out.println("You selected: Type of view");
                                break;
                            case 3:
                                System.out.println("You selected: Memory status");
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 10:
                        System.out.println("You selected: Speed dials");
                        break;
                    case 11:
                        System.out.println("You selected: Voice tags");
                        break;
                    default:
                        System.out.println("Invalid choice.");
                }
                break;
            case 2:
                System.out.println();
                System.out.println("--- MESSAGES ---");
                System.out.println("1. Write messages");
                System.out.println("2. Inbox");
                System.out.println("3. Outbox");
                System.out.println("4. Picture messages");
                System.out.println("5. Templates");
                System.out.println("6. Smileys");
                System.out.println("7. Message settings");
                System.out.println("8. Info service");
                System.out.println("9. Voice mailbox number");
                System.out.println("10. Service command editor");
                System.out.print("Enter your choice: ");
                int choice_2 = input.nextInt();

                switch (choice_2) {
                    case 1:
                        System.out.println("You selected: Write messages");
                        break;
                    case 2:
                        System.out.println("You selected: Inbox");
                        break;
                    case 3:
                        System.out.println("You selected: Outbox");
                        break;
                    case 4:
                        System.out.println("You selected: Picture messages");
                        break;
                    case 5:
                        System.out.println("You selected: Templates");
                        break;
                    case 6:
                        System.out.println("You selected: Smileys");
                        break;
                    case 7:
                        System.out.println();
                        System.out.println("--- MESSAGE SETTINGS ---");
                        System.out.println("1. Set 1");
                        System.out.println("2. Common");
                        System.out.print("Enter your choice: ");
                        int choice_2_7 = input.nextInt();

                        switch (choice_2_7) {
                            case 1:
                                System.out.println();
                                System.out.println("--- SET 1 ---");
                                System.out.println("1. Message centre number");
                                System.out.println("2. Messages sent as");
                                System.out.println("3. Message validity");
                                System.out.print("Enter your choice: ");
                                int choice_2_7_1 = input.nextInt();

                                switch (choice_2_7_1) {
                                    case 1:
                                        System.out.println("You selected: Message centre number");
                                        break;
                                    case 2:
                                        System.out.println("You selected: Messages sent as");
                                        break;
                                    case 3:
                                        System.out.println("You selected: Message validity");
                                        break;
                                    default:
                                        System.out.println("Invalid choice.");
                                }
                                break;
                            case 2:
                                System.out.println();
                                System.out.println("--- COMMON ---");
                                System.out.println("1. Delivery reports");
                                System.out.println("2. Reply via same centre");
                                System.out.println("3. Character support");
                                System.out.print("Enter your choice: ");
                                int choice_2_7_2 = input.nextInt();

                                switch (choice_2_7_2) {
                                    case 1:
                                        System.out.println("You selected: Delivery reports");
                                        break;
                                    case 2:
                                        System.out.println("You selected: Reply via same centre");
                                        break;
                                    case 3:
                                        System.out.println("You selected: Character support");
                                        break;
                                    default:
                                        System.out.println("Invalid choice.");
                                }
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 8:
                        System.out.println("You selected: Info service");
                        break;
                    case 9:
                        System.out.println("You selected: Voice mailbox number");
                        break;
                    case 10:
                        System.out.println("You selected: Service command editor");
                        break;
                    default:
                        System.out.println("Invalid choice.");
                }
                break;
            case 3:
                System.out.println("You selected: Chat");
                break;
            case 4:
                System.out.println();
                System.out.println("--- CALL REGISTER ---");
                System.out.println("1. Missed calls");
                System.out.println("2. Received calls");
                System.out.println("3. Dialled numbers");
                System.out.println("4. Erase recent call lists");
                System.out.println("5. Show call duration");
                System.out.println("6. Show call costs");
                System.out.println("7. Call cost settings");
                System.out.println("8. Prepaid credit");
                System.out.print("Enter your choice: ");
                int choice_4 = input.nextInt();

                switch (choice_4) {
                    case 1:
                        System.out.println("You selected: Missed calls");
                        break;
                    case 2:
                        System.out.println("You selected: Received calls");
                        break;
                    case 3:
                        System.out.println("You selected: Dialled numbers");
                        break;
                    case 4:
                        System.out.println("You selected: Erase recent call lists");
                        break;
                    case 5:
                        System.out.println();
                        System.out.println("--- SHOW CALL DURATION ---");
                        System.out.println("1. Last call duration");
                        System.out.println("2. All calls' duration");
                        System.out.println("3. Received calls' duration");
                        System.out.println("4. Dialled calls' duration");
                        System.out.println("5. Clear timers");
                        System.out.print("Enter your choice: ");
                        int choice_4_5 = input.nextInt();

                        switch (choice_4_5) {
                            case 1:
                                System.out.println("You selected: Last call duration");
                                break;
                            case 2:
                                System.out.println("You selected: All calls' duration");
                                break;
                            case 3:
                                System.out.println("You selected: Received calls' duration");
                                break;
                            case 4:
                                System.out.println("You selected: Dialled calls' duration");
                                break;
                            case 5:
                                System.out.println("You selected: Clear timers");
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 6:
                        System.out.println();
                        System.out.println("--- SHOW CALL COSTS ---");
                        System.out.println("1. Last call cost");
                        System.out.println("2. All calls' cost");
                        System.out.println("3. Clear counters");
                        System.out.print("Enter your choice: ");
                        int choice_4_6 = input.nextInt();

                        switch (choice_4_6) {
                            case 1:
                                System.out.println("You selected: Last call cost");
                                break;
                            case 2:
                                System.out.println("You selected: All calls' cost");
                                break;
                            case 3:
                                System.out.println("You selected: Clear counters");
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 7:
                        System.out.println();
                        System.out.println("--- CALL COST SETTINGS ---");
                        System.out.println("1. Call cost limit");
                        System.out.println("2. Show costs in");
                        System.out.print("Enter your choice: ");
                        int choice_4_7 = input.nextInt();

                        switch (choice_4_7) {
                            case 1:
                                System.out.println("You selected: Call cost limit");
                                break;
                            case 2:
                                System.out.println("You selected: Show costs in");
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 8:
                        System.out.println("You selected: Prepaid credit");
                        break;
                    default:
                        System.out.println("Invalid choice.");
                }
                break;
            case 5:
                System.out.println();
                System.out.println("--- TONES ---");
                System.out.println("1. Ringing tone");
                System.out.println("2. Ringing volume");
                System.out.println("3. Incoming call alert");
                System.out.println("4. Message alert tone");
                System.out.println("5. Keypad tones");
                System.out.println("6. Warning tones");
                System.out.println("7. Vibrating alert");
                System.out.println("8. Screen saver");
                System.out.print("Enter your choice: ");
                int choice_5 = input.nextInt();

                switch (choice_5) {
                    case 1:
                        System.out.println("You selected: Ringing tone");
                        break;
                    case 2:
                        System.out.println("You selected: Ringing volume");
                        break;
                    case 3:
                        System.out.println("You selected: Incoming call alert");
                        break;
                    case 4:
                        System.out.println("You selected: Message alert tone");
                        break;
                    case 5:
                        System.out.println("You selected: Keypad tones");
                        break;
                    case 6:
                        System.out.println("You selected: Warning tones");
                        break;
                    case 7:
                        System.out.println("You selected: Vibrating alert");
                        break;
                    case 8:
                        System.out.println("You selected: Screen saver");
                        break;
                    default:
                        System.out.println("Invalid choice.");
                }
                break;
            case 6:
                System.out.println();
                System.out.println("--- SETTINGS ---");
                System.out.println("1. Call settings");
                System.out.println("2. Phone settings");
                System.out.println("3. Security settings");
                System.out.println("4. Restore factory settings");
                System.out.print("Enter your choice: ");
                int choice_6 = input.nextInt();

                switch (choice_6) {
                    case 1:
                        System.out.println();
                        System.out.println("--- CALL SETTINGS ---");
                        System.out.println("1. Automatic redial");
                        System.out.println("2. Speed dialling");
                        System.out.println("3. Call waiting options");
                        System.out.println("4. Own number sending");
                        System.out.println("5. Phone line in use");
                        System.out.println("6. Automatic answer");
                        System.out.print("Enter your choice: ");
                        int choice_6_1 = input.nextInt();

                        switch (choice_6_1) {
                            case 1:
                                System.out.println("You selected: Automatic redial");
                                break;
                            case 2:
                                System.out.println("You selected: Speed dialling");
                                break;
                            case 3:
                                System.out.println("You selected: Call waiting options");
                                break;
                            case 4:
                                System.out.println("You selected: Own number sending");
                                break;
                            case 5:
                                System.out.println("You selected: Phone line in use");
                                break;
                            case 6:
                                System.out.println("You selected: Automatic answer");
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 2:
                        System.out.println();
                        System.out.println("--- PHONE SETTINGS ---");
                        System.out.println("1. Language");
                        System.out.println("2. Cell info display");
                        System.out.println("3. Welcome note");
                        System.out.println("4. Network selection");
                        System.out.println("5. Confirm SIM service actions");
                        System.out.print("Enter your choice: ");
                        int choice_6_2 = input.nextInt();

                        switch (choice_6_2) {
                            case 1:
                                System.out.println("You selected: Language");
                                break;
                            case 2:
                                System.out.println("You selected: Cell info display");
                                break;
                            case 3:
                                System.out.println("You selected: Welcome note");
                                break;
                            case 4:
                                System.out.println("You selected: Network selection");
                                break;
                            case 5:
                                System.out.println("You selected: Confirm SIM service actions");
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 3:
                        System.out.println();
                        System.out.println("--- SECURITY SETTINGS ---");
                        System.out.println("1. PIN code request");
                        System.out.println("2. Call barring service");
                        System.out.println("3. Fixed dialling");
                        System.out.println("4. Closed user group");
                        System.out.println("5. Security level");
                        System.out.println("6. Change access codes");
                        System.out.print("Enter your choice: ");
                        int choice_6_3 = input.nextInt();

                        switch (choice_6_3) {
                            case 1:
                                System.out.println("You selected: PIN code request");
                                break;
                            case 2:
                                System.out.println("You selected: Call barring service");
                                break;
                            case 3:
                                System.out.println("You selected: Fixed dialling");
                                break;
                            case 4:
                                System.out.println("You selected: Closed user group");
                                break;
                            case 5:
                                System.out.println("You selected: Security level");
                                break;
                            case 6:
                                System.out.println("You selected: Change access codes");
                                break;
                            default:
                                System.out.println("Invalid choice.");
                        }
                        break;
                    case 4:
                        System.out.println("You selected: Restore factory settings");
                        break;
                    default:
                        System.out.println("Invalid choice.");
                }
                break;
            case 7:
                System.out.println("You selected: Call divert");
                break;
            case 8:
                System.out.println();
                System.out.println("--- MUSIC ---");
                System.out.println("1. Music player");
                System.out.println("2. Radio");
                System.out.println("3. Recorder");
                System.out.println("4. Track list");
                System.out.print("Enter your choice: ");
                int choice_8 = input.nextInt();

                switch (choice_8) {
                    case 1:
                        System.out.println("You selected: Music player");
                        break;
                    case 2:
                        System.out.println("You selected: Radio");
                        break;
                    case 3:
                        System.out.println("You selected: Recorder");
                        break;
                    case 4:
                        System.out.println("You selected: Track list");
                        break;
                    default:
                        System.out.println("Invalid choice.");
                }
                break;
            case 9:
                System.out.println("You selected: Games");
                break;
            case 10:
                System.out.println("You selected: Calculator");
                break;
            case 11:
                System.out.println("You selected: Reminders");
                break;
            case 12:
                System.out.println();
                System.out.println("--- CLOCK ---");
                System.out.println("1. Alarm clock");
                System.out.println("2. Clock settings");
                System.out.println("3. Date setting");
                System.out.println("4. Stopwatch");
                System.out.println("5. Countdown timer");
                System.out.println("6. Auto update of date and time");
                System.out.print("Enter your choice: ");
                int choice_12 = input.nextInt();

                switch (choice_12) {
                    case 1:
                        System.out.println("You selected: Alarm clock");
                        break;
                    case 2:
                        System.out.println("You selected: Clock settings");
                        break;
                    case 3:
                        System.out.println("You selected: Date setting");
                        break;
                    case 4:
                        System.out.println("You selected: Stopwatch");
                        break;
                    case 5:
                        System.out.println("You selected: Countdown timer");
                        break;
                    case 6:
                        System.out.println("You selected: Auto update of date and time");
                        break;
                    default:
                        System.out.println("Invalid choice.");
                }
                break;
            case 13:
                System.out.println("You selected: Profiles");
                break;
            case 14:
                System.out.println("You selected: Services");
                break;
            case 15:
                System.out.println("You selected: SIM services");
                break;
            default:
                System.out.println("Invalid choice.");
        }

    }
}
