import { access, readFile } from 'node:fs/promises'
import { resolve } from 'node:path'

const root = process.cwd()
const pkg = JSON.parse(await readFile(resolve(root, 'package.json'), 'utf8'))

const requiredDependencies = ['vue', 'element-plus']
const forbiddenDependencies = ['tailwindcss', 'radix-ui', '@radix-ui/react-dialog', 'antd']
const requiredFiles = [
  'src/styles/tokens.css',
  'src/components/AppTable.vue',
  'src/components/AppDialog.vue',
  'src/views/OrdersBaseline.vue',
]

for (const name of requiredDependencies) {
  if (!pkg.dependencies?.[name]) {
    throw new Error(`missing required host dependency: ${name}`)
  }
}

for (const name of forbiddenDependencies) {
  if (pkg.dependencies?.[name] || pkg.devDependencies?.[name]) {
    throw new Error(`fixture must not contain forbidden default dependency: ${name}`)
  }
}

if (!String(pkg.packageManager || '').startsWith('pnpm@')) {
  throw new Error('fixture must pin pnpm through packageManager')
}

await Promise.all(requiredFiles.map((file) => access(resolve(root, file))))

console.log('Fixture baseline checks passed.')
