#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// initialize the tape with 30,000 zeroes
unsigned char tape[30000] = {0};
 
// set the pointer to point at the left-most cell of the tape
unsigned char* ptr = tape;


void interpret(char* input) {
    char current_char;
    size_t i;
    size_t loop;

    for (i = 0; input[i] != 0; i++) {
        current_char = input[i];
        if (current_char == '>') {
            ++ptr;
        } else if (current_char == '<') {
            --ptr;
        } else if (current_char == '+') {
            ++*ptr;
        } else if (current_char == '-') {
            --*ptr;
        } else if (current_char == '.' ) {
            putchar(*ptr);
        } else if (current_char == ',') {
            *ptr = getchar();
        } else if (current_char == '[') {
            continue;
        } else if (current_char == ']' && *ptr) {
            loop = 1;
            while (loop > 0) {
                current_char = input[--i];
                if (current_char == '[') {
                    loop--;
                } else if (current_char == ']') {
                    loop++;
                }
            }
        } else if (current_char == "$") {
            var = 1;
            unsigned char* string = "";
            while (var > 0) {
                current_char = input[++i];
                if (current_char == "0") {
                   variable_type = "str";
                }
                else if (current_char == "1") {
                   variable_type = "int";
                }
                else if (current_char == "2") {
                   variable_name = "float"
                }
                int next_char = atoi(input[++i]);
                while (next_char > 0) {
                   current_char = input[++i];
                   string = strncat(string, current_char);
                   --next_char;
                }
                --var;
            }
        } else if (current)
    }
}


int main() {
    interpret(text_to_interpret);  // outputs input
    return 0;
}
