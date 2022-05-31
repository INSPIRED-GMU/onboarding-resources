Sketchup → Collada
------------------

1. Click on the menu item **File** > **Export** > **3D Model...**.
2. Choose **COLLADA File (.dae)** as export type.
3. If you want to export the textures, click on **Options** and make sure that **Export Texture Maps** is checked.
4. Click on **Export**.

SketchUp will create a Collada file named `your-model.dae` and a folder named `your-model` that contains the model's textures.

Collada → Three.js
-------------------
Make sure you download `ColladaLoader` and include it into your project:

```html
<script type="text/javascript" src="Three.js"></script>
<script type="text/javascript" src="ColladaLoader.js"></script>
```

```javascript
var loader = new THREE.ColladaLoader();
loader.load( 'path/to/your/model.dae', function ( collada ) {

  scene.add( collada.scene );

} );
```

Note that this won't work locally because it loads the Collada file and the textures using AJAX. Therefore you have to serve the files with HTTP or change your browser's security settings as explained in [How to run things locally](https://threejs.org/docs/#manual/introduction/How-to-run-things-locally).