# Angular Code Snippet Examples

Illustrative examples of common Angular code patterns.

## Example 1: Standalone Component with Input/Output

```typescript
import { Component, input, output } from '@angular/core';
import { CommonModule } from '@angular/common'; // Import if using *ngIf, *ngFor etc.

@Component({
  selector: 'app-simple-button',
  standalone: true,
  imports: [CommonModule], // Import CommonModule if needed
  template: `
    <button (click)="handleClick()">
      {{ label() }}
    </button>
  `,
  styles: [`
    button {
      padding: 0.5em 1em;
      border-radius: 4px;
      cursor: pointer;
    }
  `]
})
export class SimpleButtonComponent {
  label = input.required<string>(); // Required input
  clicked = output<void>(); // Output event emitter

  handleClick(): void {
    this.clicked.emit();
  }
}
```

## Example 2: Service with HttpClient

```typescript
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, of } from 'rxjs';

export interface User {
  id: number;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private http = inject(HttpClient);
  private apiUrl = '/api/users'; // Example API endpoint

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl).pipe(
      catchError(this.handleError<User[]>('getUsers', []))
    );
  }

  getUser(id: number): Observable<User | undefined> {
    return this.http.get<User>(`${this.apiUrl}/${id}`).pipe(
      catchError(this.handleError<User>(`getUser id=${id}`))
    );
  }

  // Basic error handler
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(`${operation} failed: ${error.message}`);
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
```

## Example 3: Component Using Signals for State

```typescript
import { Component, signal, computed, effect, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserService, User } from './user.service'; // Assuming UserService from Example 2

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule],
  template: `
    <h2>Users</h2>
    <div *ngIf="isLoading()">Loading...</div>
    <ul *ngIf="!isLoading() && users().length > 0">
      <li *ngFor="let user of users()">{{ user.name }}</li>
    </ul>
    <div *ngIf="!isLoading() && users().length === 0">No users found.</div>
    <p>Total Users: {{ userCount() }}</p>
  `
})
export class UserListComponent {
  private userService = inject(UserService);

  users = signal<User[]>([]);
  isLoading = signal<boolean>(true);
  userCount = computed(() => this.users().length);

  constructor() {
    // Effect for logging (example side effect)
    effect(() => {
      console.log(`User count changed: ${this.userCount()}`);
    });

    // Initial data fetch
    this.loadUsers();
  }

  loadUsers(): void {
    this.isLoading.set(true);
    this.userService.getUsers().subscribe(fetchedUsers => {
      this.users.set(fetchedUsers);
      this.isLoading.set(false);
    });
  }
}
```

*(These examples illustrate basic usage. Refer to official documentation for more complex scenarios.)*