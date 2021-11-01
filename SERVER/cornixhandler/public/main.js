import * as THREE from 'three';
import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls.js';
// import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.118/build/three.module.js';
// import {OrbitControls} from 'https://cdn.jsdelivr.net/npm/three@0.118/examples/jsm/controls/OrbitControls.js';


const loader = new THREE.TextureLoader();

const scene = new THREE.Scene(); 
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 ); 
const renderer = new THREE.WebGLRenderer({ alpha: true }); 

// var light = new THREE.DirectionalLight( 0xffffff );
// light.position.set( 0, 1, 1 ).normalize();
const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1 );
scene.add(light);

scene.add(new THREE.AmbientLight(0x404040))

var geometry = new THREE.SphereGeometry(1, 32, 32);
var material = new THREE.MeshPhongMaterial()
var earthMesh = new THREE.Mesh(geometry, material);
camera.position.z = 2;

const controls = new OrbitControls( camera, renderer.domElement );

//controls.update() must be called after any manual changes to the camera's transform
//camera.position.set( 0, 20, 100 );
//controls.update();

function animate() {

    requestAnimationFrame( animate );

    // required if controls.enableDamping or controls.autoRotate are set to true
    controls.update();

    renderer.render( scene, camera );

}

material.map = loader.load('public/earthmap1k.jpg')
material.bumpMap = loader.load('public/earthbump1k.jpg')
material.bumpScale = 0.05
material.specularMap = loader.load('public/earthspec1k.jpg')
material.specular = new THREE.Color('grey')

var canvasCloud = loader.load('public/earthcloudmap.jpg')
var geometry = new THREE.SphereGeometry(0.51, 32, 32)
// var materialC = new THREE.MeshBasicMaterial( { color: 0x00ff00, opacity: 0.1 } );
var materialC = new THREE.MeshPhongMaterial({
    side : THREE.DoubleSide,
    opacity : 0.6,
    transparent : true,
    depthWrite : false,
})
materialC.map = canvasCloud
var cloudMesh = new THREE.Mesh(geometry, materialC)
earthMesh.add(cloudMesh)

// onRenderFcts.push(function(delta, now){
// earthMesh.rotation.y  += 1/32 * delta
// })
// onRenderFcts.push(function(delta, now){
// cloudMesh.rotation.y  += 1/16 * delta
// })

// create the geometry sphere
var geometry = new THREE.SphereGeometry(90, 32, 32)
// create the material, using a texture of startfield
var material = new THREE.MeshBasicMaterial({ color: 0x00ff00 })
material.map = loader.load('public/galaxy_starfield.png', function ( texture ) {
    texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
    texture.offset.set( 0, 0 );
    texture.repeat.set( 10, 10 );
    } )
material.side = THREE.BackSide
// create the mesh based on geometry and material
var mesh  = new THREE.Mesh(geometry, material)
scene.add(mesh);
scene.add(earthMesh);

renderer.setSize( window.innerWidth, window.innerHeight ); 
// renderer.setClearColor( 0x000000, 0 );
document.body.appendChild( renderer.domElement ); 