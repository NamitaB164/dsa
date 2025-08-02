//LVM

/*You are designing a virtual machine for a new programming language called Lombok. The Lombok Virtual Machine (LVM) runs an assembler-like machine code. It operates on a stack and a single register.

In detail, the instructions work as follows:

PUSH x: This instruction pushes a given integer onto the stack. If the stack for example looks like this: [2, 3] and the machine executes the instruction PUSH -11,the stack looks like this afterwards: [-11, 2, 3]

STORE: This instruction takes the topmost integer from the stack and stores it in the register. If the stack for example looks like this: [3, 9, 4], the register contains any integer, and the machine executes the instruction STORE, the stack looks like this afterwards: [9, 4] and the register contains the integer 3.

LOAD: This instruction copies the content of the register and pushes it onto the stack. If the register for example contains the integer 6, the stack looks like this: [8, 7], and the machine executes the instruction LOAD, the stack looks like this afterwards: [6, 8, 7], and the register still contains the integer 6.

PLUS: This instruction takes the two topmost integers from the stack, adds them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction PLUS, the stack looks like this afterwards: [5, 4]

TIMES: This instruction takes the two topmost integers from the stack, multiplies them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction TIMES, the stack looks like this afterwards: [6, 4]

IFZERO n: This instruction removes the topmost integer from the stack, and checks if it is equal to 0. If that is the case, it jumps to the nth instruction (start counting at 0). If not, the machine continues as usual with the next instruction. See example below.

DONE: Finally, the DONE instruction prints out the integer on top of the stack, and terminates the program regardless of the following instructions.

Computation starts with the first instruction. Initially, the stack is empty and the register contains the number 0*/




import java.io.*;
import java.util.*;

public class LombokVM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        List<String> instructions = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            instructions.add(sc.nextLine());
        }

        Stack<Integer> stack = new Stack<>();
        int register = 0;
        int ip = 0; 

        while (ip < instructions.size()) {
            String[] parts = instructions.get(ip).split(" ");
            String instr = parts[0];

            switch (instr) {
                case "PUSH":
                    int value = Integer.parseInt(parts[1]);
                    stack.push(value);
                    ip++;
                    break;

                case "STORE":
                    if (!stack.isEmpty()) {
                        register = stack.pop();
                    }
                    ip++;
                    break;

                case "LOAD":
                    stack.push(register);
                    ip++;
                    break;

                case "PLUS":
                    if (stack.size() >= 2) {
                        int a = stack.pop();
                        int b = stack.pop();
                        stack.push(a + b);
                    }
                    ip++;
                    break;

                case "TIMES":
                    if (stack.size() >= 2) {
                        int a = stack.pop();
                        int b = stack.pop();
                        stack.push(a * b);
                    }
                    ip++;
                    break;

                case "IFZERO":
                    int target = Integer.parseInt(parts[1]);
                    if (!stack.isEmpty() && stack.pop() == 0) {
                        ip = target;
                    } else {
                        ip++;
                    }
                    break;

                case "DONE":
                    if (!stack.isEmpty()) {
                        System.out.println(stack.peek());
                    }
                    return;

                default:
                    System.err.println("Unknown instruction: " + instr);
                    return;
            }
        }
    }
}