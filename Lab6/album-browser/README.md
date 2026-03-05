# Album Browser — Lab 6 (Routing & HTTP)

This project was built as part of **Web Development – Lab 6**.  
The application demonstrates Angular routing, HTTP communication, Observables, and service-based architecture.

The app fetches data from the public JSONPlaceholder REST API and implements a multi‑page Single Page Application (SPA).

---

## Application Overview

Album Browser allows users to:

- Navigate between multiple pages (Home, About, Albums)
- View a list of albums fetched from a REST API
- Open album details using route parameters
- Edit album title (PUT request)
- Delete albums from the list (DELETE request)
- View album photos using nested routing

All data is fetched from:

https://jsonplaceholder.typicode.com

Note: JSONPlaceholder simulates updates and deletions (changes are not permanently saved on the server).

---

## Implemented Routes

| Route | Description |
|--------|------------|
| `/` | Redirects to `/home` |
| `/home` | Home page |
| `/about` | About page |
| `/albums` | List of all albums |
| `/albums/:id` | Album details |
| `/albums/:id/photos` | Photos of selected album |

---

## Technologies Used

- Angular 21 (Standalone Components)
- Angular Router
- HttpClient
- RxJS Observables
- Async Pipe
- TypeScript
- CSS (component-scoped styling)

---

## Project Structure

```
src/app/
  models/
    album.model.ts
    photo.model.ts

  services/
    album.service.ts

  pages/
    home/
    about/
    albums/
    album-detail/
    album-photos/

  app.component.ts
  app.routes.ts
  app.config.ts
```

---

## Installation

Clone the repository and install dependencies:

```bash
npm install
```

---

## Running the Application

Start the development server:

```bash
ng serve
```

Open your browser at:

http://localhost:4200/

---

## Features Implemented

✔ Routing with route parameters  
✔ Nested routes (`/albums/:id/photos`)  
✔ Navigation using `routerLink` and `routerLinkActive`  
✔ HTTP requests via HttpClient  
✔ Service layer for API communication  
✔ Observables with async pipe  
✔ CRUD operations (Read, Update, Delete)  
✔ Loading indicators  
✔ Responsive photo grid layout  
✔ Clean separation of concerns  

---

## Author

Daniar Boranov  
Web Development — Lab 6  
Routing & HTTP