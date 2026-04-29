import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Task } from '../../models/task.model';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.html',
  styleUrl: './task-list.css',
  imports: [CommonModule, FormsModule]
})
export class TaskList {

  tasks = signal<Task[]>([
  { title: "Estudar Angular", done: false },
  { title: "Criar projeto", done: false },
  { title: "Treinar TypeScript", done: false }
]);

  newTask = "";

  checkedTasks: boolean[] = [];

  addTask() {

    if (this.newTask.trim() === "") return;
    this.tasks.update(tasks => [
      ...tasks,
      {title: this.newTask, done: false}
    ]);

    this.newTask = "";

  }

  removeTask(index: number) {
    this.tasks.update(tasks => tasks.filter((_, i) => i !== index));
  }
}