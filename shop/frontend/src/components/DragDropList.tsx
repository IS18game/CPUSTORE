import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable, DropResult } from 'react-beautiful-dnd';

interface Item {
  id: string;
  content: string;
}

const initialItems: Item[] = [
  { id: '1', content: 'Первый продукт' },
  { id: '2', content: 'Второй продукт' },
  { id: '3', content: 'Третий продукт' }
];

export const DragDropList: React.FC = () => {
  const [items, setItems] = useState<Item[]>(initialItems);

  const onDragEnd = (result: DropResult) => {
    if (!result.destination) return;
    const reorderedItems = Array.from(items);
    const [removed] = reorderedItems.splice(result.source.index, 1);
    reorderedItems.splice(result.destination.index, 0, removed);
    setItems(reorderedItems);
  };

  return (
    <div style={{ maxWidth: '400px', margin: 'auto' }}>
      <h3>Список продуктов (Drag & Drop)</h3>
      <DragDropContext onDragEnd={onDragEnd}>
        <Droppable droppableId="droppable">
          {(provided) => (
            <div 
              ref={provided.innerRef} 
              {...provided.droppableProps} 
              style={{ padding: 8, background: '#f0f0f0', minHeight: 100 }}
            >
              {items.map((item, index) => (
                <Draggable key={item.id} draggableId={item.id} index={index}>
                  {(provided, snapshot) => (
                    <div
                      ref={provided.innerRef}
                      {...provided.draggableProps}
                      {...provided.dragHandleProps}
                      style={{
                        userSelect: 'none',
                        padding: 16,
                        margin: '0 0 8px 0',
                        background: snapshot.isDragging ? '#263B4A' : '#456C86',
                        color: 'white',
                        ...provided.draggableProps.style
                      }}
                    >
                      {item.content}
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </div>
          )}
        </Droppable>
      </DragDropContext>
    </div>
  );
};
