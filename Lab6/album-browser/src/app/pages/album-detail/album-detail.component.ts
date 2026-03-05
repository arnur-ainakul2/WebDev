import { Component } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import { ActivatedRoute, RouterLink, RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { Observable, switchMap, map } from 'rxjs';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album.model';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterOutlet, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css'],
})
export class AlbumDetailComponent {
  album$!: Observable<Album>;
  titleDraft = '';
  saving = false;

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService,
    private location: Location
  ) {
    this.album$ = this.route.paramMap.pipe(
      map(pm => Number(pm.get('id'))),
      switchMap(id => this.albumService.getAlbum(id))
    );

    this.album$.subscribe(a => (this.titleDraft = a.title));
  }

  save(album: Album): void {
    this.saving = true;
    const updated: Album = { ...album, title: this.titleDraft };

    this.albumService.updateAlbum(updated).subscribe({
      next: () => (this.saving = false),
      error: () => (this.saving = false),
    });
  }

  back(): void {
    this.location.back();
  }
}