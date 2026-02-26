# Online Store — Lab 5 (Components & Interaction)

This project is an extended version of the Angular Online Store created in Lab 4.  
In Lab 5, the application was refactored to implement a **category-based hierarchy**, improved component architecture, and interactive features such as liking and deleting products.

---

## Overview

The application follows a structured hierarchy:

Category → Products → Product Item

Users can:

- Select a category
- View products belonging to that category
- Like products (increment counter)
- Delete products dynamically
- Share products via WhatsApp or Telegram

All products link to real items on **kaspi.kz**.

---

## Features

### Category System
- Exactly **4 categories**
- Each category contains **5 products** (20 products total)
- Dynamic rendering based on selected category
- Active category highlighting

### Component Architecture
The application contains exactly **3 components**:

1. **AppComponent**  
   - Displays categories  
   - Handles selected category  
   - Passes products to ProductListComponent  

2. **ProductListComponent**  
   - Receives products via `@Input()`  
   - Renders product items using `*ngFor`  
   - Handles delete events from child components  

3. **ProductItemComponent**  
   - Displays product details  
   - Contains Like, Delete, and Share buttons  
   - Emits delete event using `@Output()`  

---

## Interactive Features

### Like Functionality
- Each product displays a like counter (❤ likes)
- Clicking the "Like" button increments the counter
- UI updates immediately

### Delete Functionality
- Each product has a Delete button
- Product is removed dynamically from the list
- Delete event is emitted from child to parent component

### Share Functionality
- WhatsApp share link
- Telegram share link
- Uses `encodeURIComponent()` for safe URL encoding

---

## Technologies Used

- Angular 17+ (Standalone Components)
- TypeScript
- Angular Input / Output decorators
- Angular structural directives (`*ngFor`, `*ngIf`)
- CSS Grid / Flexbox
- Responsive Design

---

## Installation

Clone the repository and install dependencies:

```bash
npm install
```

---

## Running the Project

Start the development server:

```bash
ng serve
```

After the server starts, open your browser:

http://localhost:4200/

---

## Project Structure

```
src/app/
  models/
    category.model.ts
    product.model.ts

  services/
    product.service.ts

  components/
    product-list/
    product-item/

  app.component.ts
```

---

## Requirements Fulfilled

✔ 4 categories with 5 products each  
✔ 20 total products linked to real kaspi.kz items  
✔ Exactly 3 components  
✔ Parent → Child data flow using `@Input()`  
✔ Child → Parent communication using `@Output()`  
✔ Working Like feature  
✔ Working Delete feature  
✔ Clean responsive UI  
✔ Strong TypeScript typing (no `any`)  

---

## Author

Web Development — Lab 5  
Angular Components & Interaction