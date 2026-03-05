import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Observable, BehaviorSubject, combineLatest, map, startWith } from 'rxjs';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album.model';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css'],
})
export class AlbumsComponent {
  private deletedIds$ = new BehaviorSubject<Set<number>>(new Set());

  albums$: Observable<Album[]>;

  loading = true;

  constructor(private albumService: AlbumService) {
    this.albums$ = combineLatest([
      this.albumService.getAlbums().pipe(startWith(null)),
      this.deletedIds$,
    ]).pipe(
      map(([albums, deleted]) => {
        if (albums === null) return []; // пока грузится
        return albums.filter(a => !deleted.has(a.id));
      })
    );

    this.albumService.getAlbums().subscribe({
      next: () => (this.loading = false),
      error: () => (this.loading = false),
    });
  }

  deleteAlbum(id: number): void {
    this.albumService.deleteAlbum(id).subscribe({
      next: () => {
        const nextSet = new Set(this.deletedIds$.value);
        nextSet.add(id);
        this.deletedIds$.next(nextSet);
      },
    });
  }
}