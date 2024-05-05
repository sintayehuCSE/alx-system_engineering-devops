#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int infinite_while(void);
/**
 * main - Progran entry point
 *
 * Return: 0 on success, something-else otherwise
 */
int main(void)
{
	pid_t child_pid;
	int i = 0;

	for (; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid)
			printf("Zombie process created, PID: %d\n", child_pid);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
/**
 * infinite_while - Makes the process alive forever untill forcely crushed
 *
 * Return: zero (0)
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}
