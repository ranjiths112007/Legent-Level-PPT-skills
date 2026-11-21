# Asset Management, Cropping, and Placement

**Status:** Engineering reference  
**Last reviewed:** 2026-11-21

Store asset ID/path, source/provider, license/permission, generation status, model/version, prompt/settings, dimensions/format, file size/hash, alt text, slide placements and crop metadata.

## Aspect ratio
- **Contain:** preserve full image, possible empty area.
- **Cover/crop:** fill region, may trim content.
- **Native size:** use only where appropriate.

Calculate the visible crop and inspect the subject. Center crop is not always correct.

## Resolution
Use enough pixels for final displayed size. Upscaling does not guarantee detail recovery. Balance file size and clarity.

## Transparency and vectors
Transparent PNG/WebP can be useful for cutouts; verify alpha survives writer and renderer. SVG is useful for icons and diagrams but requires target-app compatibility testing.
