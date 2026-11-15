// NokiaPhone.java
// My Nokia 5510 menu map program.
// Every menu item has a number path like "6-1-2" (Settings > Call settings > Speed dialling)

import java.util.Scanner;

public class NokiaPhone {
    private String model;
    private boolean quit;     // turns true when the user types 99
    private Scanner input = new Scanner(System.in);

    public NokiaPhone(String model) {
        this.model = model;
        quit = false;
    }

    public String getModel() {
        return model;
    }

    public static void main(String[] args) {
        NokiaPhone myPhone = new NokiaPhone("Nokia 5510");
        myPhone.start();
    }

    public void start() {
        System.out.printf("Welcome to the %s menu.%n", getModel());
        mainMenu();
        System.out.println("Back to standby mode.");
    }

    // main menu (15 items)
    private void mainMenu() {
        int choice;

        do {
            showMenu("", 15);
            choice = readChoice(15);

            switch (choice) {
                case 0:
                    break;
                case 1:
                    phoneBookMenu();
                    break;
                case 2:
                    messagesMenu();
                    break;
                case 4:
                    callRegisterMenu();
                    break;
                case 5:
                    simpleMenu("5", 8);     // Tones
                    break;
                case 6:
                    settingsMenu();
                    break;
                case 8:
                    simpleMenu("8", 4);     // Music
                    break;
                case 12:
                    simpleMenu("12", 6);    // Clock
                    break;
                default:
                    runFunction("" + choice);
                    break;
            }
        } while (choice != 0 && !quit);
    }

    // 1 Phone book
    private void phoneBookMenu() {
        int choice;

        do {
            showMenu("1", 11);
            choice = readChoice(11);

            if (choice == 9) {
                simpleMenu("1-9", 3);       // Options
            } else if (choice != 0) {
                runFunction("1-" + choice);
            }
        } while (choice != 0 && !quit);
    }

    // 2 Messages
    private void messagesMenu() {
        int choice;

        do {
            showMenu("2", 10);
            choice = readChoice(10);

            if (choice == 7) {
                messageSettingsMenu();
            } else if (choice != 0) {
                runFunction("2-" + choice);
            }
        } while (choice != 0 && !quit);
    }

    // 2-7 Message settings
    private void messageSettingsMenu() {
        int choice;

        do {
            showMenu("2-7", 2);
            choice = readChoice(2);

            if (choice == 1) {
                simpleMenu("2-7-1", 3);     // Set 1
            } else if (choice == 2) {
                simpleMenu("2-7-2", 3);     // Common
            }
        } while (choice != 0 && !quit);
    }

    // 4 Call register
    private void callRegisterMenu() {
        int choice;

        do {
            showMenu("4", 8);
            choice = readChoice(8);

            switch (choice) {
                case 0:
                    break;
                case 5:
                    simpleMenu("4-5", 5);   // Show call duration
                    break;
                case 6:
                    simpleMenu("4-6", 3);   // Show call costs
                    break;
                case 7:
                    simpleMenu("4-7", 2);   // Call cost settings
                    break;
                default:
                    runFunction("4-" + choice);
                    break;
            }
        } while (choice != 0 && !quit);
    }

    // 6 Settings
    private void settingsMenu() {
        int choice;

        do {
            showMenu("6", 4);
            choice = readChoice(4);

            switch (choice) {
                case 0:
                    break;
                case 1:
                    simpleMenu("6-1", 6);   // Call settings
                    break;
                case 2:
                    simpleMenu("6-2", 5);   // Phone settings
                    break;
                case 3:
                    simpleMenu("6-3", 6);   // Security settings
                    break;
                default:
                    runFunction("6-" + choice);
                    break;
            }
        } while (choice != 0 && !quit);
    }

    // a menu where every item is a real function, no more submenus
    private void simpleMenu(String menuPath, int count) {
        int choice;

        do {
            showMenu(menuPath, count);
            choice = readChoice(count);

            if (choice != 0) {
                runFunction(menuPath + "-" + choice);
            }
        } while (choice != 0 && !quit);
    }

    // prints a menu with its title and all the items
    private void showMenu(String menuPath, int count) {
        System.out.println();
        System.out.println("==============================");

        if (menuPath.equals("")) {
            System.out.println(" MAIN MENU");
        } else {
            System.out.printf(" %s  %s%n", menuPath, itemName(menuPath).toUpperCase());
        }

        System.out.println("==============================");

        for (int i = 1; i <= count; i++) {
            String path = makePath(menuPath, i);

            if (hasSubmenu(path)) {
                printItem(i, itemName(path), true);
            } else {
                printItem(i, itemName(path));
            }
        }
    }

    // prints one item (normal item)
    private void printItem(int number, String name) {
        System.out.printf("  %2d. %s%n", number, name);
    }

    // prints one item, adds ... if it has a submenu
    private void printItem(int number, String name, boolean submenu) {
        if (submenu) {
            System.out.printf("  %2d. %s ...%n", number, name);
        } else {
            printItem(number, name);
        }
    }

    // ("6-1", 2) gives "6-1-2"
    private String makePath(String menuPath, int number) {
        if (menuPath.equals("")) {
            return "" + number;
        }
        return menuPath + "-" + number;
    }

    // asks for a number until the user types a good one
    // 0 = back, 99 = exit everything
    private int readChoice(int count) {
        int choice = 0;
        boolean ok = false;

        while (!ok) {
            System.out.print("Item number (0 = back, 99 = exit): ");

            if (input.hasNextInt()) {
                choice = input.nextInt();

                if (choice == 99) {
                    quit = true;
                    choice = 0;
                    ok = true;
                } else if (choice >= 0 && choice <= count) {
                    ok = true;
                } else {
                    System.out.printf("Enter a number from 0 to %d.%n", count);
                }
            } else {
                input.next();   // skip the wrong input
                System.out.println("Enter a number please.");
            }
        }

        return choice;
    }

    // what happens when you pick a real function
    private void runFunction(String path) {
        System.out.printf("%n*** %s ***  (shortcut %s)%n", itemName(path), path);
        System.out.println("(function would run here)");
    }

    // the menu map: path -> name
    private String itemName(String path) {
        switch (path) {
            // Phone book
            case "1":       return "Phone book";
            case "1-1":     return "Search";
            case "1-2":     return "Service Nos.";
            case "1-3":     return "Add name";
            case "1-4":     return "Erase";
            case "1-5":     return "Edit";
            case "1-6":     return "Copy";
            case "1-7":     return "Assign tone";
            case "1-8":     return "Send b'card";
            case "1-9":     return "Options";
            case "1-9-1":   return "Memory in use";
            case "1-9-2":   return "Type of view";
            case "1-9-3":   return "Memory status";
            case "1-10":    return "Speed dials";
            case "1-11":    return "Voice tags";

            // Messages
            case "2":       return "Messages";
            case "2-1":     return "Write messages";
            case "2-2":     return "Inbox";
            case "2-3":     return "Outbox";
            case "2-4":     return "Picture messages";
            case "2-5":     return "Templates";
            case "2-6":     return "Smileys";
            case "2-7":     return "Message settings";
            case "2-7-1":   return "Set 1";
            case "2-7-1-1": return "Message centre number";
            case "2-7-1-2": return "Messages sent as";
            case "2-7-1-3": return "Message validity";
            case "2-7-2":   return "Common";
            case "2-7-2-1": return "Delivery reports";
            case "2-7-2-2": return "Reply via same centre";
            case "2-7-2-3": return "Character support";
            case "2-8":     return "Info service";
            case "2-9":     return "Voice mailbox number";
            case "2-10":    return "Service command editor";

            // Chat
            case "3":       return "Chat";

            // Call register
            case "4":       return "Call register";
            case "4-1":     return "Missed calls";
            case "4-2":     return "Received calls";
            case "4-3":     return "Dialed numbers";
            case "4-4":     return "Erase recent call lists";
            case "4-5":     return "Show call duration";
            case "4-5-1":   return "Last call duration";
            case "4-5-2":   return "All calls' duration";
            case "4-5-3":   return "Received calls' duration";
            case "4-5-4":   return "Dialed calls' duration";
            case "4-5-5":   return "Clear timers";
            case "4-6":     return "Show call costs";
            case "4-6-1":   return "Last call cost";
            case "4-6-2":   return "All calls' cost";
            case "4-6-3":   return "Clear counters";
            case "4-7":     return "Call cost settings";
            case "4-7-1":   return "Call cost limit";
            case "4-7-2":   return "Show costs in";
            case "4-8":     return "Prepaid credit";

            // Tones
            case "5":       return "Tones";
            case "5-1":     return "Ringing tone";
            case "5-2":     return "Ringing volume";
            case "5-3":     return "Incoming call alert";
            case "5-4":     return "Message alert tone";
            case "5-5":     return "Keypad tones";
            case "5-6":     return "Warning tones";
            case "5-7":     return "Vibrating alert";
            case "5-8":     return "Screen saver";

            // Settings
            case "6":       return "Settings";
            case "6-1":     return "Call settings";
            case "6-1-1":   return "Automatic redial";
            case "6-1-2":   return "Speed dialing";
            case "6-1-3":   return "Call waiting options";
            case "6-1-4":   return "Own number sending";
            case "6-1-5":   return "Phone line in use";
            case "6-1-6":   return "Automatic answer";
            case "6-2":     return "Phone settings";
            case "6-2-1":   return "Language";
            case "6-2-2":   return "Cell info display";
            case "6-2-3":   return "Welcome note";
            case "6-2-4":   return "Network selection";
            case "6-2-5":   return "Confirm SIM service actions";
            case "6-3":     return "Security settings";
            case "6-3-1":   return "PIN code request";
            case "6-3-2":   return "Call barring service";
            case "6-3-3":   return "Fixed dialing";
            case "6-3-4":   return "Closed user group";
            case "6-3-5":   return "Security level";
            case "6-3-6":   return "Change access codes";
            case "6-4":     return "Restore factory settings";

            // 7 to 15
            case "7":       return "Call divert";
            case "8":       return "Music";
            case "8-1":     return "Music player";
            case "8-2":     return "Radio";
            case "8-3":     return "Recorder";
            case "8-4":     return "Track list";
            case "9":       return "Games";
            case "10":      return "Calculator";
            case "11":      return "Reminders";
            case "12":      return "Clock";
            case "12-1":    return "Alarm clock";
            case "12-2":    return "Clock settings";
            case "12-3":    return "Date setting";
            case "12-4":    return "Stopwatch";
            case "12-5":    return "Countdown timer";
            case "12-6":    return "Auto update of date and time";
            case "13":      return "Profiles";
            case "14":      return "Services";
            case "15":      return "SIM services";

            default:        return "";
        }
    }

    // true if this item opens another menu
    private boolean hasSubmenu(String path) {
        switch (path) {
            case "1": case "2": case "4": case "5": case "6": case "8": case "12":
            case "1-9":
            case "2-7": case "2-7-1": case "2-7-2":
            case "4-5": case "4-6": case "4-7":
            case "6-1": case "6-2": case "6-3":
                return true;
            default:
                return false;
        }
    }
}// NokiaPhone.java
// My Nokia 5510 menu map program.
// Every menu item has a number path like "6-1-2" (Settings > Call settings > Speed dialling)

