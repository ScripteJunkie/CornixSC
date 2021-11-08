import React, { Component } from "react";
import ReactDOM from "react-dom";
import * as THREE from "three";
import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls.js';


import earthmap1k from './assets/earthmap1k.jpg';
import earthbump1k from './assets/earthbump1k.jpg';
import earthspec1k from './assets/earthspec1k.jpg';
import earthcloudmap from './assets/earthcloudmap.jpg';
import sunText from './assets/SunText.jpeg';
// import galaxy_starfield from './assets/galaxy_starfield.png';

class App extends Component {

  planetToggle = (e) => {
    // camera.
  }


    componentDidMount() {

        const raycaster = new THREE.Raycaster();
        const mouse = new THREE.Vector2();

        const loader = new THREE.TextureLoader();
      
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
        var renderer = new THREE.WebGLRenderer( { antialias: true } ); // { alpha: true } makes background transparent
        renderer.setSize( window.innerWidth, window.innerHeight );
        this.mount.appendChild( renderer.domElement );
        
        // Stanton
        var geometrySun = new THREE.SphereGeometry(5, 64, 64);
        var materialSun = new THREE.MeshStandardMaterial({
          color: new THREE.Color(0xffe6a1),
          emissiveIntensity: 1,
          emissive: new THREE.Color(0xf7c740),
        });
        materialSun.map = loader.load(sunText);
        var sunMesh = new THREE.Mesh(geometrySun, materialSun);
        scene.add(sunMesh);

        // Arccorp
        var geometryEarth = new THREE.SphereGeometry(0.5, 64, 64);
        var materialEarth = new THREE.MeshPhongMaterial()
        var earthMesh = new THREE.Mesh(geometryEarth, materialEarth);

        const controls = new OrbitControls( camera, renderer.domElement );

        // controls.update() // must be called after any manual changes to the camera's transform
        // camera.position.set( 0, 20, 100 );
        // controls.update();

        materialEarth.map = loader.load(earthmap1k)
        materialEarth.bumpMap = loader.load(earthbump1k)
        materialEarth.bumpScale = 0.05
        materialEarth.specularMap = loader.load(earthspec1k)
        materialEarth.specular = new THREE.Color('grey')

        var canvasCloud = loader.load(earthcloudmap)
        var geometryCloud = new THREE.SphereGeometry(0.51, 64, 64)
        // var materialC = new THREE.MeshBasicMaterial( { color: 0x00ff00, opacity: 0.1 } );
        var materialC = new THREE.MeshPhongMaterial({
            side : THREE.DoubleSide,
            opacity : 0.6,
            transparent : true,
            depthWrite : false,
        })
        materialC.map = canvasCloud
        var cloudMesh = new THREE.Mesh(geometryCloud, materialC)
        earthMesh.add(cloudMesh)

        // onRenderFcts.push(function(delta, now){
        // earthMesh.rotation.y  += 1/32 * delta
        // })
        // onRenderFcts.push(function(delta, now){
        // cloudMesh.rotation.y  += 1/16 * delta
        // })

        // create the geometry sphere
        // var geometry = new THREE.SphereGeometry(90, 32, 32)
        // // create the material, using a texture of startfield
        // var material = new THREE.MeshBasicMaterial({ color: 0x00ff00 })
        // material.map = loader.load(galaxy_starfield, function ( texture ) {
        //     texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
        //     texture.offset.set( 0, 0 );
        //     texture.repeat.set( 10, 10 );
        //     } )
        // material.side = THREE.BackSide
        // // create the mesh based on geometry and material
        // var mesh  = new THREE.Mesh(geometry, material)
        // scene.add(mesh);
        scene.add(earthMesh);
        earthMesh.position.z = 15;

        earthMesh.rotateZ(0.131);

        var geometry2 = new THREE.SphereGeometry( 0.5, 64, 64 );
        var material2 = new THREE.MeshPhongMaterial( { color: 0x7e31eb } );
        var Planet2 = new THREE.Mesh( geometry2, material2 );

        scene.add(Planet2);
        Planet2.position.x = 20;
        
        // const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1 );
        // scene.add( light );
        // var light = new THREE.DirectionalLight( 0xffffff );
        var light = new THREE.PointLight( 0xffe6a1, 2);
        light.position.set( 0, 0, 0 ).normalize();
        scene.add( light );
        var light2 = new THREE.AmbientLight( 0xffe6a1, 0.2);
        scene.add( light2 );

        camera.position.z = 20;
        camera.position.x = 20;

        // controls.update() // must be called after any manual changes to the camera's transform
        // controls.target.set( Planet2.position.x, Planet2.position.y, Planet2.position.z );
        controls.update();

        var animate = function () {
            requestAnimationFrame( animate );
            earthMesh.rotation.y += 0.001;
            renderer.render( scene, camera );
        };
        animate();

        function onMouseDown( e ) {
          mouse.x = ( e.clientX / window.innerWidth ) * 2 - 1;
          mouse.y = - ( e.clientY / window.innerHeight ) * 2 + 1;
          // console.log(mouse.x, mouse.y);
          window.requestAnimationFrame(render);
        }

        function render() {
				  camera.updateMatrixWorld();
          // update the picking ray with the camera and mouse position
          raycaster.setFromCamera( mouse, camera );
				  const intersects = raycaster.intersectObjects( scene.children );
          if ( intersects.length > 0 ) {
                  intersects[ 0 ].object.material.emissive.setHex( Math.random() * 0xffffff );
              }
          if (typeof intersects[ 0 ] !== 'undefined') {
              console.log(intersects[ 0 ]);
              // controls.target.set( intersects[ 0 ] );
              // console.log( camera.position );
            }
            // camera.lookAt( intersects[ 0 ] );
          }
        window.addEventListener( 'click', onMouseDown );r
    }

    render() {
        return (
            <div>
              <button style={{bottom: "0px", position: "absolute", padding: "5px"}} onClick={this.planetToggle}>
                <span className="material-icons">
                  Gallery
                </span>
              </button>
              <div ref={ref => (this.mount = ref)} />
            </div>
        )
    }
}
const rootElement = document.getElementById("root")
ReactDOM.render(<App />, rootElement);
export default App;

// // import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//           <script src='main.js' type='module'></script>
//     </div>
//   );
// }

// export default App;