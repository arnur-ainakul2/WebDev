import { Component,Input,OnInit} from '@angular/core';
import {Product} from '../../product.model';
@Component({
  selector: 'app-product-card',
  imports: [],
  templateUrl: './product-card.html',
  styleUrl: './product-card.css',
})
export class ProductCard {
  @Input() product!: Product;

  getStars(): string[] {
    const stars = [];
    for (let i = 1; i <= 5; i++) {
      stars.push(i <= Math.round(this.product.rating) ? '★' : '☆');
    }
    return stars;
  }

  getWhatsAppLink(): string {
    return `https://wa.me/?text=${encodeURIComponent('Check out this product: ' + this.product.link)}`;
  }
  selectedImage: string = '';

  ngOnInit() {
    this.selectedImage = this.product.image;
  }

  selectImage(image: string) {
    this.selectedImage = image;
  }
}
