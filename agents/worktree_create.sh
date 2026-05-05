#!/bin/bash
name=$1
task_id=$2
REPO_ROOT="/Users/jiezhao/Documents/demo/agentfwk/learn-claude-code/agents/REPO_ROOT"
worktree_dir="$REPO_ROOT/worktrees/$name"

if [ ! -d "$worktree_dir" ]; then
  git worktree add "$worktree_dir" --name "$name" --no-overlay
  echo "Created worktree: $name"
else
  echo "Worktree $name already exists"
fi

echo "{\"timestamp\":\"$(date -Is)\",\"type\":\"worktree_create\",\"name\":\"$name\",\"task_id\":\"$task_id\"}" >> .worktrees/events.jsonl