This file is a merged representation of the entire codebase, combined into a single document by Repomix.
The content has been processed where content has been compressed (code blocks are separated by ⋮---- delimiter).

<file_summary>
This section contains a summary of this file.

<purpose>
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.
</purpose>

<file_format>
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files, each consisting of:
  - File path as an attribute
  - Full contents of the file
</file_format>

<usage_guidelines>
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.
</usage_guidelines>

<notes>
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Content has been compressed - code blocks are separated by ⋮---- delimiter
- Files are sorted by Git change count (files with more changes are at the bottom)
</notes>

<additional_info>

</additional_info>

</file_summary>

<directory_structure>
src/
  tools/
    answer_query_direct.ts
    answer_query_websearch.ts
    architecture_pattern_recommendation.ts
    code_analysis_with_docs.ts
    database_schema_analyzer.ts
    dependency_vulnerability_scan.ts
    directory_tree.ts
    documentation_generator.ts
    edit_file.ts
    execute_terminal_command.ts
    explain_topic_with_docs.ts
    generate_project_guidelines.ts
    get_doc_snippets.ts
    get_file_info.ts
    index.ts
    list_directory.ts
    microservice_design_assistant.ts
    move_file.ts
    read_file.ts
    regulatory_compliance_advisor.ts
    save_answer_query_direct.ts
    save_answer_query_websearch.ts
    save_doc_snippet.ts
    save_generate_project_guidelines.ts
    save_topic_explanation.ts
    search_files.ts
    security_best_practices_advisor.ts
    technical_comparison.ts
    testing_strategy_generator.ts
    tool_definition.ts
    write_file.ts
  config.ts
  index.ts
  utils.ts
  vertex_ai_client.ts
.env.example
.gitignore
Dockerfile
LICENSE
package.json
README.md
smithery.yaml
tsconfig.json
</directory_structure>

<files>
This section contains the contents of the repository's files.

<file path="src/tools/answer_query_direct.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/answer_query_websearch.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/architecture_pattern_recommendation.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/code_analysis_with_docs.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/database_schema_analyzer.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/dependency_vulnerability_scan.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/directory_tree.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition (adapted from example.ts) - Exported
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "get_directory_tree", // Renamed slightly
⋮----
inputSchema: DirectoryTreeJsonSchema as any, // Cast as any if needed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// No 'execute' function here
</file>

<file path="src/tools/documentation_generator.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/edit_file.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definitions (adapted from example.ts) - Exported
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "edit_file_content", // Renamed slightly
⋮----
inputSchema: EditFileJsonSchema as any, // Cast as any if needed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// Add a check for empty edits array
⋮----
// No 'execute' function here
</file>

<file path="src/tools/execute_terminal_command.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "execute_terminal_command", // Renamed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// No 'execute' function here
</file>

<file path="src/tools/explain_topic_with_docs.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/generate_project_guidelines.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
⋮----
// Enhanced System Instruction for Guideline Generation
⋮----
// Enhanced User Query for Guideline Generation
</file>

<file path="src/tools/get_doc_snippets.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
⋮----
// Enhanced System Instruction for precise documentation snippets
⋮----
// Enhanced User Query for precise documentation snippets
</file>

<file path="src/tools/get_file_info.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition (adapted from example.ts) - Exported
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "get_filesystem_info", // Renamed slightly
⋮----
inputSchema: GetFileInfoJsonSchema as any, // Cast as any if needed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// No 'execute' function here
</file>

<file path="src/tools/index.ts">
import { ToolDefinition } from "./tool_definition.js";
import { answerQueryWebsearchTool } from "./answer_query_websearch.js";
import { answerQueryDirectTool } from "./answer_query_direct.js";
import { explainTopicWithDocsTool } from "./explain_topic_with_docs.js";
import { getDocSnippetsTool } from "./get_doc_snippets.js";
import { generateProjectGuidelinesTool } from "./generate_project_guidelines.js";
// Filesystem Tools (Imported)
import { readFileTool } from "./read_file.js"; // Handles single and multiple files now
// import { readMultipleFilesTool } from "./read_multiple_files.js"; // Merged into readFileTool
import { writeFileTool } from "./write_file.js";
import { editFileTool } from "./edit_file.js";
// import { createDirectoryTool } from "./create_directory.js"; // Removed
import { listDirectoryTool } from "./list_directory.js";
import { directoryTreeTool } from "./directory_tree.js";
import { moveFileTool } from "./move_file.js";
import { searchFilesTool } from "./search_files.js";
import { getFileInfoTool } from "./get_file_info.js";
import { executeTerminalCommandTool } from "./execute_terminal_command.js"; // Renamed file and tool variable
// Import the new combined tools
import { saveGenerateProjectGuidelinesTool } from "./save_generate_project_guidelines.js";
import { saveDocSnippetTool } from "./save_doc_snippet.js";
import { saveTopicExplanationTool } from "./save_topic_explanation.js";
// Removed old save_query_answer, added new specific ones
import { saveAnswerQueryDirectTool } from "./save_answer_query_direct.js";
import { saveAnswerQueryWebsearchTool } from "./save_answer_query_websearch.js";
⋮----
// Import new research-oriented tools
import { codeAnalysisWithDocsTool } from "./code_analysis_with_docs.js";
import { technicalComparisonTool } from "./technical_comparison.js";
import { architecturePatternRecommendationTool } from "./architecture_pattern_recommendation.js";
import { dependencyVulnerabilityScanTool } from "./dependency_vulnerability_scan.js";
import { databaseSchemaAnalyzerTool } from "./database_schema_analyzer.js";
import { securityBestPracticesAdvisorTool } from "./security_best_practices_advisor.js";
import { testingStrategyGeneratorTool } from "./testing_strategy_generator.js";
import { regulatoryComplianceAdvisorTool } from "./regulatory_compliance_advisor.js";
import { microserviceDesignAssistantTool } from "./microservice_design_assistant.js";
import { documentationGeneratorTool } from "./documentation_generator.js";
⋮----
// Query & Generation Tools
⋮----
// Filesystem Tools
readFileTool, // Handles single and multiple files now
// readMultipleFilesTool, // Merged into readFileTool
⋮----
// createDirectoryTool, // Removed
⋮----
executeTerminalCommandTool, // Renamed
// Add the new combined tools
⋮----
// Removed old save_query_answer, added new specific ones
⋮----
// New research-oriented tools
⋮----
// Create a map for easy lookup
</file>

<file path="src/tools/list_directory.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition (adapted from example.ts) - Exported
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "list_directory_contents", // Renamed slightly
⋮----
inputSchema: ListDirectoryJsonSchema as any, // Cast as any if needed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// No 'execute' function here
</file>

<file path="src/tools/microservice_design_assistant.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/move_file.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition (adapted from example.ts) - Exported
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "move_file_or_directory", // Renamed slightly
⋮----
inputSchema: MoveFileJsonSchema as any, // Cast as any if needed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// Add check: source and destination cannot be the same
⋮----
// No 'execute' function here
</file>

<file path="src/tools/read_file.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
// Note: We don't need fs, path here as execution logic is moved
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition (adapted from example.ts) - Exported
⋮----
// Infer the input type for validation
type ReadFileInput = z.infer<typeof ReadFileArgsSchema>;
⋮----
// Convert Zod schema to JSON schema for the tool definition
⋮----
name: "read_file_content", // Keep the name consistent
⋮----
// Use the converted JSON schema
inputSchema: ReadFileJsonSchema as any, // Cast as any to fit ToolDefinition if needed
⋮----
// This tool doesn't directly use the LLM, so buildPrompt is minimal/not used for execution
⋮----
// Basic validation
⋮----
// Use InternalError or InvalidParams
⋮----
// No prompt generation needed for direct execution logic
⋮----
systemInstructionText: "", // Not applicable
userQueryText: "", // Not applicable
⋮----
// Removed the 'execute' function - this logic will go into src/index.ts
</file>

<file path="src/tools/regulatory_compliance_advisor.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/save_answer_query_direct.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema for direct query answer + output path
⋮----
// Convert Zod schema to JSON schema
⋮----
const { query } = parsed.data; // output_path used in handler
⋮----
// --- Use Prompt Logic from answer_query_direct.ts ---
⋮----
useWebSearch: false, // Hardcoded to false
</file>

<file path="src/tools/save_answer_query_websearch.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema for websearch query answer + output path
⋮----
// Convert Zod schema to JSON schema
⋮----
const { query } = parsed.data; // output_path used in handler
⋮----
// --- Use Prompt Logic from answer_query_websearch.ts ---
⋮----
useWebSearch: true, // Always true for this tool
</file>

<file path="src/tools/save_doc_snippet.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema combining get_doc_snippets args + output_path
⋮----
// Convert Zod schema to JSON schema
⋮----
// Build prompt logic - Reverted to the stricter version (98/100 rating)
⋮----
// Validate args using the combined schema
⋮----
// Destructure validated args (output_path is used in handler, not prompt)
⋮----
// --- Use the Stricter Prompt Logic ---
⋮----
// Return the prompt components needed by the handler
⋮----
useWebSearch: true, // Always use web search for snippets
</file>

<file path="src/tools/save_generate_project_guidelines.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema for combined arguments
⋮----
// Convert Zod schema to JSON schema
⋮----
// This buildPrompt function contains the core logic for generating the AI prompt.
// The main handler in index.ts will call this *part* of the logic.
⋮----
// Validate args using the combined schema
⋮----
const { tech_stack } = parsed.data; // output_path is used in the handler, not the prompt
⋮----
// --- Use the Updated Prompt Logic Provided by User ---
⋮----
// Return the prompt components needed by the handler
⋮----
useWebSearch: true, // Always use web search for guidelines
enableFunctionCalling: false // No function calling needed for generation
</file>

<file path="src/tools/save_topic_explanation.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema combining explain_topic_with_docs args + output_path
⋮----
// Convert Zod schema to JSON schema
⋮----
// Build prompt logic adapted from explain_topic_with_docs (Reverted to original working version)
⋮----
const { topic, query } = parsed.data; // output_path used in handler
⋮----
6.  **Format:** Use Markdown for formatting.`; // Reverted: Removed the \"CRITICAL: Do NOT start...\" instruction
⋮----
const userQueryText = `Provide a comprehensive explanation for the query \"${query}\" regarding the software topic \"${topic}\". Base the explanation primarily on official documentation found via web search. Include relevant concepts, code examples (if available in docs), and cite sources.`; // Reverted: Removed the extra instruction about starting format
⋮----
useWebSearch: true, // Always use web search for explanations based on docs
</file>

<file path="src/tools/search_files.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition (adapted from example.ts) - Exported
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "search_filesystem", // Renamed slightly
⋮----
inputSchema: SearchFilesJsonSchema as any, // Cast as any if needed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// No 'execute' function here
</file>

<file path="src/tools/security_best_practices_advisor.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/technical_comparison.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/testing_strategy_generator.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
</file>

<file path="src/tools/tool_definition.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { Content, Tool } from "@google-cloud/vertexai";
⋮----
export interface ToolDefinition {
    name: string;
    description: string;
    inputSchema: any; // Consider defining a stricter type like JSONSchema7
    buildPrompt: (args: any, modelId: string) => {
        systemInstructionText: string;
        userQueryText: string;
        useWebSearch: boolean;
        enableFunctionCalling: boolean;
    };
}
⋮----
inputSchema: any; // Consider defining a stricter type like JSONSchema7
⋮----
export const modelIdPlaceholder = "${modelId}"; // Placeholder for dynamic model ID in descriptions
⋮----
// Helper to build the initial content array
export function buildInitialContent(systemInstruction: string, userQuery: string): Content[]
⋮----
// Helper to determine tools for API call
export function getToolsForApi(enableFunctionCalling: boolean, useWebSearch: boolean): Tool[] | undefined
⋮----
// Function calling is no longer supported by the remaining tools
return useWebSearch ? [{ googleSearch: {} } as any] : undefined; // Cast needed as SDK type might not include googleSearch directly
</file>

<file path="src/tools/write_file.ts">
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
import { ToolDefinition, modelIdPlaceholder } from "./tool_definition.js";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";
⋮----
// Schema definition (adapted from example.ts) - Exported
// Schema for a single file write operation
⋮----
// Schema for the arguments object, containing either a single write or an array of writes
⋮----
// Convert Zod schema to JSON schema
⋮----
name: "write_file_content", // Keep name consistent
⋮----
inputSchema: WriteFileJsonSchema as any, // Cast as any if needed
⋮----
// Minimal buildPrompt as execution logic is separate
⋮----
// No 'execute' function here
</file>

<file path="src/config.ts">
// Correctly import Gemini types only from @google/generative-ai
import { HarmCategory as GenaiHarmCategory, HarmBlockThreshold as GenaiHarmBlockThreshold } from "@google/generative-ai";
⋮----
// --- Provider Configuration ---
export type AIProvider = "vertex" | "gemini";
⋮----
// --- Vertex AI Specific ---
⋮----
// --- Gemini API Specific ---
⋮----
// --- Common AI Configuration Defaults ---
⋮----
// --- Safety Settings ---
// For Vertex AI (@google-cloud/vertexai)
⋮----
// For Gemini API (@google/generative-ai) - using corrected imports
⋮----
// --- Validation ---
⋮----
// --- Shared Config Retrieval ---
export function getAIConfig()
⋮----
// Common parameters
⋮----
// Temperature range varies, allow 0-2 for Gemini flexibility
⋮----
// Provider-specific model ID
⋮----
} else { // gemini
⋮----
// Provider-specific connection info
</file>

<file path="src/index.ts">
import dotenv from 'dotenv';
import path from 'path';
⋮----
// Load .env file from the current working directory (where npx/node is run)
// This ensures it works correctly when run via npx outside the project dir
⋮----
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  McpError,
  ErrorCode,
} from "@modelcontextprotocol/sdk/types.js";
// Removed vertexai Content import as CombinedContent covers it
import fs from "fs/promises";
import { z } from "zod"; // Needed for schema parsing within handler
import { diffLines, createTwoFilesPatch } from 'diff';
import { minimatch } from 'minimatch';
import { exec } from 'child_process'; // Added for command execution
import util from 'util'; // Added for promisify
⋮----
import { getAIConfig } from './config.js';
// Import CombinedContent along with callGenerativeAI
import { callGenerativeAI, CombinedContent } from './vertex_ai_client.js';
import { allTools, toolMap } from './tools/index.js';
import { buildInitialContent, getToolsForApi } from './tools/tool_definition.js';
⋮----
// Import Zod schemas from tool files for validation within the handler
import { ReadFileArgsSchema } from './tools/read_file.js';
// import { ReadMultipleFilesArgsSchema } from './tools/read_multiple_files.js'; // Removed
import { WriteFileArgsSchema } from './tools/write_file.js';
import { EditFileArgsSchema, EditOperationSchema } from './tools/edit_file.js'; // Import EditOperationSchema too
// import { CreateDirectoryArgsSchema } from './tools/create_directory.js'; // Removed
import { ListDirectoryArgsSchema } from './tools/list_directory.js';
import { DirectoryTreeArgsSchema } from './tools/directory_tree.js';
import { MoveFileArgsSchema } from './tools/move_file.js';
import { SearchFilesArgsSchema } from './tools/search_files.js';
import { GetFileInfoArgsSchema } from './tools/get_file_info.js';
// Import schemas for the new combined tools
import { SaveGenerateProjectGuidelinesArgsSchema } from './tools/save_generate_project_guidelines.js';
import { SaveDocSnippetArgsSchema } from './tools/save_doc_snippet.js';
import { SaveTopicExplanationArgsSchema } from './tools/save_topic_explanation.js';
import { SaveAnswerQueryDirectArgsSchema } from './tools/save_answer_query_direct.js';
import { SaveAnswerQueryWebsearchArgsSchema } from './tools/save_answer_query_websearch.js';
import { ExecuteTerminalCommandArgsSchema } from './tools/execute_terminal_command.js'; // Renamed
⋮----
// --- Filesystem Helper Functions (Adapted from example.ts) ---
⋮----
// Basic security check - ensure path stays within workspace
function validateWorkspacePath(requestedPath: string): string
⋮----
interface FileInfo {
  size: number;
  created: Date;
  modified: Date;
  accessed: Date;
  isDirectory: boolean;
  isFile: boolean;
  permissions: string;
}
⋮----
async function getFileStats(filePath: string): Promise<FileInfo>
⋮----
permissions: stats.mode.toString(8).slice(-3), // POSIX permissions
⋮----
async function searchFilesRecursive(
  rootPath: string,
  currentPath: string,
  pattern: string,
  excludePatterns: string[],
  results: string[]
): Promise<void>
⋮----
function normalizeLineEndings(text: string): string
⋮----
function createUnifiedDiff(originalContent: string, newContent: string, filepath: string = 'file'): string
⋮----
async function applyFileEdits(
  filePath: string,
  edits: z.infer<typeof EditOperationSchema>[],
  dryRun = false
): Promise<string>
⋮----
interface TreeEntry {
    name: string;
    type: 'file' | 'directory';
    children?: TreeEntry[];
}
⋮----
async function buildDirectoryTree(currentPath: string): Promise<TreeEntry[]>
⋮----
// Set of filesystem tool names for easy checking
⋮----
"read_file_content", // Handles single/multiple
// "read_multiple_files_content", // Removed
"write_file_content", // Handles single/multiple
⋮----
// "create_directory", // Removed
⋮----
// --- MCP Server Setup ---
⋮----
// --- Tool Definitions Handler ---
⋮----
// Use new config function
⋮----
// Inject model ID dynamically from new config structure
⋮----
// --- Tool Call Handler ---
⋮----
// --- Special Handling for Combined Tool ---
⋮----
// Use new config function
⋮----
// Use new AI function call and type cast
⋮----
// Config args removed
⋮----
} // --- Filesystem Tool Execution Logic ---
⋮----
// Handle single file read
⋮----
// Handle multiple file read (similar to old read_multiple_files_content)
⋮----
// case "read_multiple_files_content": // Removed - logic merged into read_file_content
⋮----
// Access the 'writes' property which contains either a single object or an array
⋮----
// case "create_directory": // Removed
⋮----
// Return successful filesystem operation result
⋮----
} else if (toolName === "execute_terminal_command") { // Renamed tool name check
const parsed = ExecuteTerminalCommandArgsSchema.parse(args); // Renamed schema
⋮----
options.cwd = validateWorkspacePath(parsed.cwd); // Reuse validation
⋮----
options.cwd = process.cwd(); // Default to workspace root
⋮----
options.timeout = parsed.timeout * 1000; // Convert seconds to milliseconds
⋮----
// Execute the command
⋮----
// Handle different error types
⋮----
// The finally block might not be strictly necessary here as execPromise handles cleanup
// if (controller) { controller.abort(); } // Example if manual cleanup were needed
⋮----
// --- Generic AI Tool Logic (Non-filesystem, non-combined) ---
const config = getAIConfig(); // Use renamed config function
⋮----
const initialContents = buildInitialContent(systemInstructionText, userQueryText) as CombinedContent[]; // Cast
⋮----
// Call the unified AI function
⋮----
// Config is implicitly used by callGenerativeAI now
⋮----
// Centralized error handling
⋮----
// --- Server Start ---
async function main()
⋮----
// --- Graceful Shutdown ---
const shutdown = async (signal: string) =>
</file>

<file path="src/utils.ts">
import { WORKSPACE_ROOT } from './config.js';
⋮----
export const sleep = (ms: number)
⋮----
// Basic path validation
export function sanitizePath(inputPath: string): string
⋮----
// Basic check against path traversal
</file>

<file path="src/vertex_ai_client.ts">
// Correct import: Use @google/generative-ai
import { GoogleGenerativeAI } from "@google/generative-ai";
// Import specific types needed, alias Content and explicitly import SafetySetting
import type { Content as GoogleGeneraiContent, GenerationConfig, SafetySetting, FunctionDeclaration } from "@google/generative-ai";
⋮----
import { McpError, ErrorCode } from "@modelcontextprotocol/sdk/types.js";
// Import getAIConfig and original safety setting definitions from config
import { getAIConfig, vertexSafetySettings, geminiSafetySettings as configGeminiSafetySettings } from './config.js';
import { sleep } from './utils.js';
⋮----
// --- Configuration and Client Initialization ---
⋮----
// Use correct client types
⋮----
} else { // gemini
⋮----
// Instantiate using the correct package
⋮----
// Define a union type for Content
export type CombinedContent = vertexAiSdk.Content | GoogleGeneraiContent;
⋮----
// --- Unified AI Call Function ---
export async function callGenerativeAI(
    initialContents: CombinedContent[],
    tools: vertexAiSdk.Tool[] | undefined // Still expect Vertex Tool format initially
): Promise<string>
⋮----
tools: vertexAiSdk.Tool[] | undefined // Still expect Vertex Tool format initially
⋮----
adaptedToolsForGemini = undefined; // Keep undefined for now
⋮----
// Get appropriate model instance
⋮----
} else { // gemini
⋮----
// Safety settings/genConfig are passed to generateContent for @google/generative-ai
⋮----
// --- Prepare Request Parameters (differ slightly between SDKs) ---
⋮----
// Use the correctly typed settings imported from config
⋮----
// Safety settings variable is not needed, pass directly below
⋮----
safetySettings: resolvedVertexSafetySettings, // Pass correct settings
⋮----
// @google/generative-ai takes config in generateContent call
⋮----
// --- Execute Request with Retries ---
⋮----
// Simplified log line without the problematic length check
⋮----
} else { // gemini
⋮----
// tools: adaptedToolsForGemini,
⋮----
} else { // Non-streaming
⋮----
} else { // gemini
⋮----
// tools: adaptedToolsForGemini,
⋮----
// --- Return Text ---
⋮----
} // End retry loop
</file>

<file path=".env.example">
# Environment variables for vertex-ai-mcp-server
# --- Required ---
# REQUIRED only if AI_PROVIDER is \"vertex\"
GOOGLE_CLOUD_PROJECT=\"YOUR_GCP_PROJECT_ID\"
# REQUIRED only if AI_PROVIDER is \"gemini\"
GEMINI_API_KEY=\"YOUR_GEMINI_API_KEY\" # Get from Google AI Studio

# --- General AI Configuration ---
AI_PROVIDER=\"vertex\" # Provider to use: \"vertex\" or \"gemini\"
# Optional - Model ID depends on the chosen provider
VERTEX_MODEL_ID=\"gemini-2.5-pro-exp-03-25\" # e.g., gemini-1.5-pro-latest, gemini-1.0-pro
GEMINI_MODEL_ID=\"gemini-2.5-pro-exp-03-25\" # e.g., gemini-2.5-pro-exp-03-25, gemini-pro

# --- Optional AI Parameters (Common) ---
# GOOGLE_CLOUD_LOCATION is specific to Vertex AI
GOOGLE_CLOUD_LOCATION=\"us-central1\"
AI_TEMPERATURE=\"0.0\"         # Range: 0.0 to 1.0
AI_USE_STREAMING=\"true\"      # Use streaming responses: \"true\" or \"false\"
AI_MAX_OUTPUT_TOKENS=\"65536\" # Max tokens in response (Note: Models have their own upper limits)
AI_MAX_RETRIES=\"3\"           # Number of retries on transient errors
AI_RETRY_DELAY_MS=\"1000\"     # Delay between retries in milliseconds

# --- Optional Vertex AI Authentication ---
# Uncomment and set if using a Service Account Key instead of Application Default Credentials (ADC) for Vertex AI
# GOOGLE_APPLICATION_CREDENTIALS=\"/path/to/your/service-account-key.json\"
</file>

<file path=".gitignore">
node_modules/
build/
*.log
.env*
!.env.example
*.zip
*.md
!README.md
</file>

<file path="Dockerfile">
# Generated by https://smithery.ai. See: https://smithery.ai/docs/config#dockerfile
# Build stage
FROM node:lts-alpine AS build
WORKDIR /app

# Install dependencies without running prepare scripts
COPY package.json tsconfig.json bun.lock .
RUN npm install --ignore-scripts

# Copy source and transpile
COPY . .
RUN npx tsc -p tsconfig.json && chmod +x build/index.js

# Production image
FROM node:lts-alpine
WORKDIR /app

# Copy built application
COPY --from=build /app/build ./build

# Install production dependencies without running prepare scripts
COPY package.json bun.lock .
RUN npm install --omit=dev --ignore-scripts

ENV NODE_ENV=production
ENTRYPOINT [\"node\", \"build/index.js\"]
</file>

<file path="LICENSE">
Copyright (c) 2025 Shariq Riaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</file>

<file path="package.json">
{
  \"name\": \"vertex-ai-mcp-server\",
  \"version\": \"0.3.5\",
  \"description\": \"A Model Context Protocol server supporting Vertex AI and Gemini API\",
  \"license\": \"MIT\",
  \"type\": \"module\",
  \"bin\": {
    \"vertex-ai-mcp-server\": \"build/index.js\"
  },
  \"repository\": {
    \"type\": \"git\",
    \"url\": \"git+https://github.com/shariqriazz/vertex-ai-mcp-server.git\"
  },
  \"homepage\": \"https://github.com/shariqriazz/vertex-ai-mcp-server#readme\",
  \"bugs\": {
    \"url\": \"https://github.com/shariqriazz/vertex-ai-mcp-server/issues\"
  },
  \"files\": [
    \"build\"
  ],
  \"scripts\": {
    \"build\": \"bun run tsc && node -e \\\"require('fs').chmodSync('build/index.js', '755')\\\"\",
    \"prepare\": \"bun run build\",
    \"watch\": \"bun run tsc --watch\",
    \"inspector\": \"bunx @modelcontextprotocol/inspector build/index.js\"
  },
  \"dependencies\": {
    \"@google-cloud/vertexai\": \"^1.9.3\",
    \"@google/generative-ai\": \"^0.17.0\",
    \"@modelcontextprotocol/sdk\": \"0.6.0\",
    \"diff\": \"^7.0.0\",
    \"dotenv\": \"^16.5.0\",
    \"minimatch\": \"^10.0.1\",
    \"zod\": \"^3.24.3\",
    \"zod-to-json-schema\": \"^3.24.5\"
  },
  \"devDependencies\": {
    \"@types/diff\": \"^7.0.2\",
    \"@types/minimatch\": \"^5.1.2\",
    \"@types/node\": \"^20.11.24\",
    \"typescript\": \"^5.3.3\"
  }
}
</file>

<file path="README.md">
# Vertex AI MCP Server
[![smithery badge](https://smithery.ai/badge/@shariqriazz/vertex-ai-mcp-server)](https://smithery.ai/server/@shariqriazz/vertex-ai-mcp-server)

This project implements a Model Context Protocol (MCP) server that provides a comprehensive suite of tools for interacting with Google Cloud's Vertex AI Gemini models, focusing on coding assistance and general query answering.

<a href="https://glama.ai/mcp/servers/@shariqriazz/vertex-ai-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@shariqriazz/vertex-ai-mcp-server/badge" alt="Vertex AI Server MCP server" />
</a>

## Features

*   Provides access to Vertex AI Gemini models via numerous MCP tools.
*   Supports web search grounding (`answer_query_websearch`) and direct knowledge answering (`answer_query_direct`).
*   Configurable model ID, temperature, streaming behavior, max output tokens, and retry settings via environment variables.
*   Uses streaming API by default for potentially better responsiveness.
*   Includes basic retry logic for transient API errors.
*   Minimal safety filters applied (`BLOCK_NONE`) to reduce potential blocking (use with caution).

## Tools Provided

### Query & Generation (AI Focused)
*   `answer_query_websearch`: Answers a natural language query using the configured Vertex AI model enhanced with Google Search results.
*   `answer_query_direct`: Answers a natural language query using only the internal knowledge of the configured Vertex AI model.
*   `explain_topic_with_docs`: Provides a detailed explanation for a query about a specific software topic by synthesizing information primarily from official documentation found via web search.
*   `get_doc_snippets`: Provides precise, authoritative code snippets or concise answers for technical queries by searching official documentation.
*   `generate_project_guidelines`: Generates a structured project guidelines document (Markdown) based on a specified list of technologies (optionally with versions), using web search for best practices.

### Research & Analysis Tools
*   `code_analysis_with_docs`: Analyzes code snippets by comparing them with best practices from official documentation, identifying potential bugs, performance issues, and security vulnerabilities.
*   `technical_comparison`: Compares multiple technologies, frameworks, or libraries based on specific criteria, providing detailed comparison tables with pros/cons and use cases.
*   `architecture_pattern_recommendation`: Suggests architecture patterns for specific use cases based on industry best practices, with implementation examples and considerations.
*   `dependency_vulnerability_scan`: Analyzes project dependencies for known security vulnerabilities, providing detailed information and mitigation strategies.
*   `database_schema_analyzer`: Reviews database schemas for normalization, indexing, and performance issues, suggesting improvements based on database-specific best practices.
*   `security_best_practices_advisor`: Provides security recommendations for specific technologies or scenarios, with code examples for implementing secure practices.
*   `testing_strategy_generator`: Creates comprehensive testing strategies for applications or features, suggesting appropriate testing types with coverage goals.
*   `regulatory_compliance_advisor`: Provides guidance on regulatory requirements for specific industries (GDPR, HIPAA, etc.), with implementation approaches for compliance.
*   `microservice_design_assistant`: Helps design microservice architectures for specific domains, with service boundary recommendations and communication patterns.
*   `documentation_generator`: Creates comprehensive documentation for code, APIs, or systems, following industry best practices for technical documentation.

### Filesystem Operations
*   `read_file_content`: Read the complete contents of one or more files. Provide a single path string or an array of path strings.
*   `write_file_content`: Create new files or completely overwrite existing files. The 'writes' argument accepts a single object (`{path, content}`) or an array of such objects.
*   `edit_file_content`: Makes line-based edits to a text file, returning a diff preview or applying changes.
*   `list_directory_contents`: Lists files and directories directly within a specified path (non-recursive).
*   `get_directory_tree`: Gets a recursive tree view of files and directories as JSON.
*   `move_file_or_directory`: Moves or renames files and directories.
*   `search_filesystem`: Recursively searches for files/directories matching a name pattern, with optional exclusions.
*   `get_filesystem_info`: Retrieves detailed metadata (size, dates, type, permissions) about a file or directory.
*   `execute_terminal_command`: Execute a shell command, optionally specifying `cwd` and `timeout`. Returns stdout/stderr.

### Combined AI + Filesystem Operations
*   `save_generate_project_guidelines`: Generates project guidelines based on a tech stack and saves the result to a specified file path.
*   `save_doc_snippet`: Finds code snippets from documentation and saves the result to a specified file path.
*   `save_topic_explanation`: Generates a detailed explanation of a topic based on documentation and saves the result to a specified file path.
*   `save_answer_query_direct`: Answers a query using only internal knowledge and saves the answer to a specified file path.
*   `save_answer_query_websearch`: Answers a query using web search results and saves the answer to a specified file path.

*(Note: Input/output schemas for each tool are defined in their respective files within `src/tools/` and exposed via the MCP server.)*

## Prerequisites

*   Node.js (v18+)
*   Bun (`npm install -g bun`)
*   Google Cloud Project with Billing enabled.
*   Vertex AI API enabled in the GCP project.
*   Google Cloud Authentication configured in your environment (Application Default Credentials via `gcloud auth application-default login` is recommended, or a Service Account Key).

## Setup & Installation

1.  **Clone/Place Project:** Ensure the project files are in your desired location.
2.  **Install Dependencies:**
    ```bash
    bun install
    ```
3.  **Configure Environment:**
    *   Create a `.env` file in the project root (copy `.env.example`).
    *   Set the required and optional environment variables as described in `.env.example`.
        *   Set `AI_PROVIDER` to either `\"vertex\"` or `\"gemini\"`.
        *   If `AI_PROVIDER=\"vertex\"`, `GOOGLE_CLOUD_PROJECT` is required.
        *   If `AI_PROVIDER=\"gemini\"`, `GEMINI_API_KEY` is required.
4.  **Build the Server:**
    ```bash
    bun run build
    ```
    This compiles the TypeScript code to `build/index.js`.

## Usage (Standalone / NPX)

Once published to npm, you can run this server directly using `npx`:

```bash
# Ensure required environment variables are set (e.g., GOOGLE_CLOUD_PROJECT)
bunx vertex-ai-mcp-server
```

Alternatively, install it globally:

```bash
bun install -g vertex-ai-mcp-server
# Then run:
vertex-ai-mcp-server
```

**Note:** Running standalone requires setting necessary environment variables (like `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, authentication credentials if not using ADC) in your shell environment before executing the command.

### Installing via Smithery

To install Vertex AI Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@shariqriazz/vertex-ai-mcp-server):

```bash
bunx -y @smithery/cli install @shariqriazz/vertex-ai-mcp-server --client claude
```

## Running with Cline

1.  **Configure MCP Settings:** Add/update the configuration in your Cline MCP settings file (e.g., `.roo/mcp.json`). You have two primary ways to configure the command:

    **Option A: Using Node (Direct Path - Recommended for Development)**

    This method uses `node` to run the compiled script directly. It's useful during development when you have the code cloned locally.

    ```json
    {
      \"mcpServers\": {
        \"vertex-ai-mcp-server\": {
          \"command\": \"node\",
          \"args\": [
            \"/full/path/to/your/vertex-ai-mcp-server/build/index.js\" // Use absolute path or ensure it's relative to where Cline runs node
          ],
          \"env\": {
            // --- General AI Configuration ---
            \"AI_PROVIDER\": \"vertex\", // \"vertex\" or \"gemini\"
            // --- Required (Conditional) ---
            \"GOOGLE_CLOUD_PROJECT\": \"YOUR_GCP_PROJECT_ID\", // Required if AI_PROVIDER=\"vertex\"
            // \"GEMINI_API_KEY\": \"YOUR_GEMINI_API_KEY\", // Required if AI_PROVIDER=\"gemini\"
            // --- Optional Model Selection ---
            \"VERTEX_MODEL_ID\": \"gemini-2.5-pro-exp-03-25\", // If AI_PROVIDER=\"vertex\" (Example override)
            \"GEMINI_MODEL_ID\": \"gemini-2.5-pro-exp-03-25\", // If AI_PROVIDER=\"gemini\"
            // --- Optional AI Parameters ---
            \"GOOGLE_CLOUD_LOCATION\": \"us-central1\", // Specific to Vertex AI
            \"AI_TEMPERATURE\": \"0.0\",
            \"AI_USE_STREAMING\": \"true\",
            \"AI_MAX_OUTPUT_TOKENS\": \"65536\", // Default from .env.example
            \"AI_MAX_RETRIES\": \"3\",
            \"AI_RETRY_DELAY_MS\": \"1000\",
            // --- Optional Vertex Authentication ---
            // \"GOOGLE_APPLICATION_CREDENTIALS\": \"/path/to/your/service-account-key.json\" // If using Service Account Key for Vertex
          },
          \"disabled\": false,
          \"alwaysAllow\": [
             // Add tool names here if you don't want confirmation prompts
             // e.g., \"answer_query_websearch\"
          ],
          \"timeout\": 3600 // Optional: Timeout in seconds
        }
        // Add other servers here...
      }
    }
    ```
    *   **Important:** Ensure the `args` path points correctly to the `build/index.js` file. Using an absolute path might be more reliable.

    **Option B: Using NPX (Requires Package Published to npm)**

    This method uses `npx` to automatically download and run the server package from the npm registry. This is convenient if you don't want to clone the repository.

    ```json
    {
      \"mcpServers\": {
        \"vertex-ai-mcp-server\": {
          \"command\": \"bunx\", // Use bunx
          \"args\": [
            \"-y\", // Auto-confirm installation
            \"vertex-ai-mcp-server\" // The npm package name
          ],
          \"env\": {
            // --- General AI Configuration ---
            \"AI_PROVIDER\": \"vertex\", // \"vertex\" or \"gemini\"
            // --- Required (Conditional) ---
            \"GOOGLE_CLOUD_PROJECT\": \"YOUR_GCP_PROJECT_ID\", // Required if AI_PROVIDER=\"vertex\"
            // \"GEMINI_API_KEY\": \"YOUR_GEMINI_API_KEY\", // Required if AI_PROVIDER=\"gemini\"
            // --- Optional Model Selection ---
            \"VERTEX_MODEL_ID\": \"gemini-2.5-pro-exp-03-25\", // If AI_PROVIDER=\"vertex\" (Example override)
            \"GEMINI_MODEL_ID\": \"gemini-2.5-pro-exp-03-25\", // If AI_PROVIDER=\"gemini\"
            // --- Optional AI Parameters ---
            \"GOOGLE_CLOUD_LOCATION\": \"us-central1\", // Specific to Vertex AI
            \"AI_TEMPERATURE\": \"0.0\",
            \"AI_USE_STREAMING\": \"true\",
            \"AI_MAX_OUTPUT_TOKENS\": \"65536\", // Default from .env.example
            \"AI_MAX_RETRIES\": \"3\",
            \"AI_RETRY_DELAY_MS\": \"1000\",
            // --- Optional Vertex Authentication ---
            // \"GOOGLE_APPLICATION_CREDENTIALS\": \"/path/to/your/service-account-key.json\" // If using Service Account Key for Vertex
          },
          \"disabled\": false,
          \"alwaysAllow\": [
             // Add tool names here if you don't want confirmation prompts
             // e.g., \"answer_query_websearch\"
          ],
          \"timeout\": 3600 // Optional: Timeout in seconds
        }
        // Add other servers here...
      }
    }
    ```
    *   Ensure the environment variables in the `env` block are correctly set, either matching `.env` or explicitly defined here. Remove comments from the actual JSON file.

2.  **Restart/Reload Cline:** Cline should detect the configuration change and start the server.

3.  **Use Tools:** You can now use the extensive list of tools via Cline.

## Development

*   **Watch Mode:** `bun run watch`
*   **Linting:** `bun run lint`
*   **Formatting:** `bun run format`
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
</file>

<file path="smithery.yaml">
# Smithery configuration file: https://smithery.ai/docs/config#smitheryyaml

startCommand:
  type: stdio
  configSchema:
    # JSON Schema defining the configuration options for the MCP.
    type: object
    required:
      - googleCloudProject
      - googleCloudLocation
    properties:
      googleCloudProject:
        type: string
        description: Google Cloud Project ID
      googleCloudLocation:
        type: string
        description: Google Cloud Location
      googleApplicationCredentials:
        type: string
        description: Path to service account key JSON
      vertexAiModelId:
        type: string
        default: gemini-2.5-pro-exp-03-25
        description: Vertex AI Model ID
      vertexAiTemperature:
        type: number
        default: 0
        description: Temperature for model
      vertexAiUseStreaming:
        type: boolean
        default: true
        description: Whether to use streaming
      vertexAiMaxOutputTokens:
        type: number
        default: 65535
        description: Max output tokens
      vertexAiMaxRetries:
        type: number
        default: 3
        description: Max retry attempts
      vertexAiRetryDelayMs:
        type: number
        default: 1000
        description: Delay between retries in ms
  commandFunction:
    # A JS function that produces the CLI command based on the given config to start the MCP on stdio.
    |-
    (config) => ({ command: 'node', args: ['build/index.js'], env: { ...(config.googleCloudProject && { GOOGLE_CLOUD_PROJECT: config.googleCloudProject }), ...(config.googleCloudLocation && { GOOGLE_CLOUD_LOCATION: config.googleCloudLocation }), ...(config.googleApplicationCredentials && { GOOGLE_APPLICATION_CREDENTIALS: config.googleApplicationCredentials }), ...(config.vertexAiModelId && { VERTEX_AI_MODEL_ID: config.vertexAiModelId }), ...(config.vertexAiTemperature !== undefined && { VERTEX_AI_TEMPERATURE: String(config.vertexAiTemperature) }), ...(config.vertexAiUseStreaming !== undefined && { VERTEX_AI_USE_STREAMING: String(config.vertexAiUseStreaming) }), ...(config.vertexAiMaxOutputTokens !== undefined && { VERTEX_AI_MAX_OUTPUT_TOKENS: String(config.vertexAiMaxOutputTokens) }), ...(config.vertexAiMaxRetries !== undefined && { VERTEX_AI_MAX_RETRIES: String(config.vertexAiMaxRetries) }), ...(config.vertexAiRetryDelayMs !== undefined && { VERTEX_AI_RETRY_DELAY_MS: String(config.vertexAiRetryDelayMs) }) } })
  exampleConfig:
    googleCloudProject: my-gcp-project
    googleCloudLocation: us-central1
    googleApplicationCredentials: /path/to/credentials.json
    vertexAiModelId: gemini-2.5-pro-exp-03-25
    vertexAiTemperature: 0
    vertexAiUseStreaming: true
    vertexAiMaxOutputTokens: 65535
    vertexAiMaxRetries: 3
    vertexAiRetryDelayMs: 1000
</file>

<file path="tsconfig.json">
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
</file>

</files>