import { createBrowserRouter } from 'react-router-dom';
import Layout from './Layout';
import HomePage from '../components/HomePage/HomePage';
import AlbumListings from '../components/AlbumListings/AlbumListings';
import AlbumDetails from '../components/Album/AlbumDetails';
import UserProfile from '../components/UserProfile/UserProfile';
import Checkout from '../components/Checkout/Checkout';
import About from '../components/Footer/About';
import { albumLoader } from './album';
import ManageSupportedBys from '../components/SupportedBy/ManageSupportedBys';
import { getSupportedBys } from './supportedbys';


export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: '/',
        element: <HomePage />,
        loader: async () => {
          return await fetch('/api/albums')
        }
      },
      {
        path: "/albums",
        element: <AlbumListings />,
        loader: async () => {
          return await fetch("/api/albums")
        }
      },
      {
        path: "/albums/:albumId",
        element: <AlbumDetails />,
        loader: albumLoader
      },
      // {
      //   path: "/albums/new",
      //   element: <CreateAlbumFormModal/>
      // },
      {
        path: "/user",
        element: <UserProfile />,
        loader: async () => {
          return await fetch("/api/albums")
        }
      },
      {
        path: "/checkout",
        element: <Checkout />
      },
      {
        path: "/user/reviews",
        element: <ManageSupportedBys />,
        loader: getSupportedBys
      },
      {
        path: "/about",
        element: <About />
      }
    ]
  },
  {
    path: "*",
    element: <h1>404 Not Found</h1>
  }
]);
