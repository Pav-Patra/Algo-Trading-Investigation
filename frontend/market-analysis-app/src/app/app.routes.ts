import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        pathMatch: 'full',
        loadComponent: () => {
            return import('./home/home.component').then((m) => m.HomeComponent)
        }
    },
    {
        path: 'asset',
        loadComponent: () => {
            return import('./asset/asset.component').then((m) => m.AssetComponent)
        }
    }
];
