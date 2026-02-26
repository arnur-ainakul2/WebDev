import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Category } from './models/category.model';
import { Product } from './models/product.model';
import { ProductService } from './services/product.service';
import { ProductListComponent } from './components/product-list/product-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ProductListComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  categories: Category[] = [];
  selectedCategoryId: number | null = null;
  visibleProducts: Product[] = [];

  constructor(private productService: ProductService) {
    this.categories = this.productService.getCategories();
  }

  selectCategory(cat: Category): void {
    this.selectedCategoryId = cat.id;
    this.visibleProducts = this.productService.getProductsByCategory(cat.id);
    console.log('Selected category:', cat, 'products:', this.visibleProducts);
  }
}