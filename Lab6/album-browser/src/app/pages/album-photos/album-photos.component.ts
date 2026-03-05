import { Component } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { Observable, map, switchMap } from 'rxjs';
import { AlbumService } from '../../services/album.service';
import { Photo } from '../../models/photo.model';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css'],
})
export class AlbumPhotosComponent {
  photos$!: Observable<Photo[]>;
  loading = true;

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService,
    private location: Location
  ) {
    this.photos$ = this.route.parent!.paramMap.pipe(
      map(pm => Number(pm.get('id'))),
      switchMap(id => this.albumService.getAlbumPhotos(id))
    );

    this.photos$.subscribe({
      next: () => (this.loading = false),
      error: () => (this.loading = false),
    });
  }

  back(): void {
    this.location.back();
  }
}