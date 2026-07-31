#!/usr/bin/env node
import { lstatSync, mkdirSync, readlinkSync, symlinkSync, unlinkSync } from "node:fs";
import { homedir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const target = path.resolve(process.env.SKILLS_HOME || path.join(process.env.CODEX_HOME || path.join(homedir(), ".codex"), "skills"));
const forceLinks = process.argv.includes("--force-links");
const entry = "full-stack-development-workflow";
const retired = [
  "full-stack-requirements",
  "full-stack-implementation",
  "full-stack-debugging",
  "full-stack-quality-review",
  "full-stack-deployment",
];

function statOrNull(file) {
  try { return lstatSync(file); } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

mkdirSync(target, { recursive: true });

for (const name of retired) {
  const link = path.join(target, name);
  const stat = statOrNull(link);
  if (!stat?.isSymbolicLink()) continue;
  const destination = path.resolve(path.dirname(link), readlinkSync(link));
  if (destination === path.join(root, "skills", name)) {
    unlinkSync(link);
    console.log(`retired ${name}`);
  }
}

const source = path.join(root, "skills", entry);
const link = path.join(target, entry);
const stat = statOrNull(link);
if (stat) {
  const same = stat.isSymbolicLink() && path.resolve(path.dirname(link), readlinkSync(link)) === source;
  if (same) {
    console.log(`ok ${entry}`);
    process.exit(0);
  }
  if (!forceLinks || !stat.isSymbolicLink()) throw new Error(`${link} exists and is not the managed link`);
  unlinkSync(link);
}
symlinkSync(source, link, "dir");
console.log(`installed ${entry}`);
