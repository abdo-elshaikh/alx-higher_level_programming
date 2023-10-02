#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - function in C that checks if a singly linked list has a cycle in it.
 * @list: single linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
    listint_t *slow;
    listint_t *fast;

    while (list && list->next)
    {
        slow = list->next;
        fast = list->next->next;
        if (slow == fast)
            return (1);
    }
    return (0);
}

