#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *aux;
    int len, i, *copy;

    if (!*head || !head)
        return (1);
    aux = *head;
    for (len = 1; aux->next; len++)
        aux = aux->next;
    copy = malloc(sizeof(int) * (len));
    if (!copy)
        return (-1);
    for (i = 0, aux = *head; i < len; i++, aux = aux->next)
        copy[i] = aux->n;
    for (i = 0; i < (len / 2); i++)
        if (copy[i] != copy[len - 1 - i])
        {
            free(copy);
            return (0);
        }
    free(copy);
    return (1);
}
