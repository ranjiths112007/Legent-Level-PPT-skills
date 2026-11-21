# Asset Management, Cropping, and Placement

Store asset ID/path, source/provider, license, generation status, model/version, prompt/settings, dimensions/format, file size/hash, alt text, placements and crop metadata.

Aspect handling:
- **Contain:** preserve full image; empty area possible.
- **Cover/crop:** fill target; may trim content.
- **Native size:** only when appropriate.

Calculate visible crop and inspect subject; center crop is not always correct. Use enough pixels for final displayed size; upscaling does not guarantee detail recovery. Balance size and clarity.

Transparent PNG/WebP can help cutouts; verify alpha survives writer and renderer. SVG is useful for icons/diagrams but requires target-app compatibility testing.