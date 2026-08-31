// Read-only relocation-aware wrapper. No frozen dossier checker is modified or executed.
import {verify} from "./preservation_lib.mjs";
console.log(JSON.stringify(verify(),null,2));
