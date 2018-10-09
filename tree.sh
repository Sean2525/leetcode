#!/bin/bash

echo "# LeetCode" > README.md
echo "\`\`\`bash" >> README.md
tree --noreport | sed '1d' >> README.md
echo "\`\`\`" >> README.md
