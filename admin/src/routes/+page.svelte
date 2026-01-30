<script lang="ts">

</script>

<div class="container">
    <h1>Todos & Tasks</h1>

    <div class="add-todo">
        <a class="button-link" href="/todo">Todo</a>
        <a class="button-link" href="/task">Task</a>
    </div>

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

    .add-todo {
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

    .todo-list {
        list-style: none;
        padding: 0;
    }

    .todo-list li {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        border-bottom: 1px solid #eee;
    }

    .todo-list li span {
        flex: 1;
    }

    .todo-list li.completed span {
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