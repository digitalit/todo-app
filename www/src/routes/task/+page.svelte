<script lang="ts">
    import {onMount} from 'svelte';
    import {getFastAPI} from '$lib/api/gen/fastAPI';
    import type {Task} from '$lib/api/gen/model';

    const api = getFastAPI();

    let tasks = $state<Task[]>([]);
    let newTaskTitle = $state('');
    let loading = $state(false);

    async function loadTasks() {
        loading = true;
        try {
            const response = await api.wwwListTasks();
            tasks = response.data;
        } catch (error) {
            console.error('Failed to load task:', error);
        } finally {
            loading = false;
        }
    }

    async function addTask() {
        if (!newTaskTitle.trim()) return;

        try {
            const response = await api.wwwCreateTask({
                title: newTaskTitle,
                completed: false
            });
            tasks = [...tasks, response.data];
            newTaskTitle = '';
        } catch (error) {
            console.error('Failed to create task:', error);
        }
    }

    async function toggleTask(task: Task) {
        try {
            const response = await api.wwwUpdateTask(task.id, {
                completed: !task.completed
            });
            tasks = tasks.map((t) => (t.id === task.id ? response.data : t));
        } catch (error) {
            console.error('Failed to update task:', error);
        }
    }

    async function removeTask(id: number) {
        try {
            await api.wwwDeleteTask(id);
            tasks = tasks.filter((t) => t.id !== id);
        } catch (error) {
            console.error('Failed to delete task:', error);
        }
    }

    onMount(() => {
        loadTasks();
    });
</script>

<div class="container">
    <h1>Task List www</h1>

    <a class="button-link" href="/">Home</a>
    <a class="button-link" href="/todo">Todo</a>
    <br>
    <div class="add-task">
        <input
                type="text"
                bind:value={newTaskTitle}
                placeholder="What needs to be done?"
                onkeydown={(e) => e.key === 'Enter' && addTask()}
        />
        <button onclick={addTask}>Add</button>
    </div>

    {#if loading}
        <p>Loading...</p>
    {:else if tasks.length === 0}
        <p class="empty">No tasks yet. Add one above!</p>
    {:else}
        <ul class="task-list">
            {#each tasks as task (task.id)}
                <li class:completed={task.completed}>
                    <input
                            type="checkbox"
                            checked={task.completed}
                            onchange={() => toggleTask(task)}
                    />
                    <span>{task.title}</span>
                    <button class="delete" onclick={() => removeTask(task.id)}>
                        ×
                    </button>
                </li>
            {/each}
        </ul>
    {/if}
</div>

<style>
    .container {
        max-width: 600px;
        margin: 2rem auto;
        padding: 2rem;
    }

    h1 {
        text-align: center;
        color: #333;
    }

    .add-task {
        display: flex;
        gap: 0.5rem;
        margin: 2rem 0;
    }

    input[type='text'] {
        flex: 1;
        padding: 0.75rem;
        border: 2px solid #ddd;
        border-radius: 4px;
        font-size: 1rem;
    }

    button {
        padding: 0.75rem 1.5rem;
        background: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1rem;
    }

    button:hover {
        background: #0056b3;
    }

    .task-list {
        list-style: none;
        padding: 0;
    }

    .task-list li {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        border-bottom: 1px solid #eee;
    }

    .task-list li span {
        flex: 1;
    }

    .task-list li.completed span {
        text-decoration: line-through;
        color: #999;
    }

    .delete {
        background: #dc3545;
        padding: 0.25rem 0.75rem;
        font-size: 1.5rem;
        line-height: 1;
    }

    .delete:hover {
        background: #c82333;
    }

    .empty {
        text-align: center;
        color: #999;
        padding: 2rem;
    }
</style>