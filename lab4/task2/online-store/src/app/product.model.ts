export interface Product{
  id:number; //unique identifier
  name:string; //product name
  description:string; //short product descrip
  price:number;
  rating:number;
  image: string //Url or local path
  images:string[] //array of images URLs for the gallery
  link:string //direct url
}
