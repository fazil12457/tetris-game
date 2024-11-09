#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define constants for transaction thresholds
#define MAX_TRANSACTION_AMOUNT 10000  // Maximum allowed transaction
#define MAX_TRANSACTION_COUNT 5      // Maximum number of transactions in a short period (e.g., 24 hours)
#define SUSPICIOUS_ACTIVITY_THRESHOLD 3 // Number of suspicious activities to flag fraud

// Structure to hold transaction details
typedef struct {
    int transaction_id;
    int account_id;
    float amount;
    char date[11];  // Date in "YYYY-MM-DD" format
    char type[10];  // Transaction type (Deposit/Withdrawal)
} Transaction;

// Function to check if a transaction is suspicious
int is_suspicious(Transaction t) {
    if (t.amount > MAX_TRANSACTION_AMOUNT) {
        printf("Suspicious: Transaction amount %.2f exceeds the limit.\n", t.amount);
        return 1;  // Suspicious transaction
    }
    return 0;  // Not suspicious
}

// Function to check for multiple suspicious activities in a short period
int check_multiple_suspicious_transactions(Transaction* transactions, int n) {
    int suspicious_count = 0;

    for (int i = 0; i < n; i++) {
        if (is_suspicious(transactions[i])) {
            suspicious_count++;
        }
    }

    // If there are multiple suspicious transactions, flag as fraud
    if (suspicious_count >= SUSPICIOUS_ACTIVITY_THRESHOLD) {
        printf("Fraud detected: Multiple suspicious activities within a short period.\n");
        return 1;
    }

    return 0;
}

int main() {
    // Example list of transactions (in a real application, this would come from a database)
    Transaction transactions[] = {
        {1, 1001, 12000.0, "2024-11-01", "Withdrawal"},
        {2, 1001, 5000.0, "2024-11-01", "Deposit"},
        {3, 1001, 7000.0, "2024-11-02", "Withdrawal"},
        {4, 1002, 10000.0, "2024-11-02", "Withdrawal"},
        {5, 1001, 15000.0, "2024-11-03", "Deposit"}
    };

    int n = sizeof(transactions) / sizeof(transactions[0]);

    // Check for suspicious transactions
    if (check_multiple_suspicious_transactions(transactions, n)) {
        printf("Fraud detected in transaction data.\n");
    } else {
        printf("No fraud detected.\n");
    }

    return 0;
}
