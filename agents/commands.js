function handleCompleteTask(taskId) {
  const taskFile = `/tasks/${taskId}.json`;
  const task = readJson(taskFile);
  if (task.status !== 'in_progress') {
    throw new Error('Task not in progress');
  }
  task.status = 'completed';
  writeJson(taskFile, task);
  runWorktreeRemove(task.worktreeName);
}

// Register command
handleCommand('complete_task', handleCompleteTask);