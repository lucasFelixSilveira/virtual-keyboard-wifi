#include <stdio.h>
#include <stdlib.h>

void run();

void restart() {
    run();
}

void run() {
    #if defined(_WIN32)
        system("cls");
    #else
        system("clear");
    #endif

    printf("0 - Enter key\n1 - Type\n");
    int action = 0;
    scanf("%d", &action);

    switch(action) {
        case 0: { // Enter
            system("node enter.js");
            restart();
            break;
        }
        case 1: { // Type
            printf("Typed> ");

            int c;
            while ((c = getchar()) != '\n' && c != EOF) {}
            char col[1024];
            fgets(col, sizeof(col), stdin);

            printf("typed now: %s", col);

            printf("Press any key to send.");
            fflush(stdout); 
            getchar();

            char cli[1124];
            sprintf(cli, "node send.js %s", col);
            system(cli);
            restart();
            break;
        }
        default:
            printf("Invalid action.\n");
            restart();
    }
}

int main() {
    run();
    return 0;
}